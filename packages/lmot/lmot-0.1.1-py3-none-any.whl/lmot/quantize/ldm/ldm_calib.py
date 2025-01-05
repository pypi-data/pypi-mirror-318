import torch
import logging
import json
from lmot.quantize.ldm.ldm_quant import LDMQuantizer
from lmot.quantize.ldm.utils import to_float8
from typing import List

from diffusers.utils import load_image

import torch
import numpy as np
import cv2
from PIL import Image

logger = logging.getLogger(__name__)

class LDMCalibrator(LDMQuantizer):
    def __init__(self, args):
        super().__init__(args)
        self.all_act_range = {}
        self.all_act_range_controlnet = None
        self.all_kl_div = {}
        self.calculate_kl_divergence = False

    def model_quantize(self):
        if self.args.model_architecture == "sdxl":
            hooked_model = self.pipe.unet
        elif self.args.model_architecture == "sdxl-controlnet":
            hooked_model = self.pipe.unet
            hooked_model_controlnet = self.pipe.controlnet
            self.all_act_range_controlnet = {}
        else:
            hooked_model = self.pipe.transformer

        if self.args.act_range_file is not None:
            self.all_act_range = read_act_scale(self.args.act_range_file)
            self.calculate_kl_divergence = True

        # Register a hook for each layer
        for name, layer in hooked_model.named_modules():
            layer.__name__ = name
            if self.calculate_kl_divergence:
                layer.register_forward_hook(self.get_kl_divergence)
            else:
                layer.register_forward_hook(self.get_activation_range)

        if self.args.model_architecture == "sdxl-controlnet":
            for name, layer in hooked_model_controlnet.named_modules():
                layer.__name__ = name
                layer.register_forward_hook(self.get_activation_range_controlnet)

        # get model activation range
        gen = torch.Generator().manual_seed(self.args.seed)
        if "sdxl-controlnet" == self.args.model_architecture:
            image = image = load_image(self.args.controlnet_image_path)
            image = np.array(image)
            image = cv2.Canny(image, 100, 200)
            image = image[:, :, None]
            image = np.concatenate([image, image, image], axis=2)
            image = Image.fromarray(image)

            images = self.pipe(
                prompt=self.args.prompts, negative_prompt=self.args.negative_prompts, 
                um_inference_steps=self.args.steps, image=image, 
                generator=gen, width=self.args.width, height=self.args.height, 
                controlnet_conditioning_scale=0.5,
                ).images[0]
        else:
            if self.args.ipadapter_model_path is not None:
                image = load_image(self.args.ipadapter_image_path)
                images = self.pipe(
                    prompt=self.args.prompts, 
                    num_inference_steps=self.args.steps, 
                    ip_adapter_image=image, 
                    negative_prompt=self.args.negative_prompts,
                    generator=gen
                ).images[0]
            else:
                images = self.pipe(prompt=self.args.prompts, 
                                   num_inference_steps=self.args.steps, 
                                   generator=gen, width=self.args.width, 
                                   height=self.args.height).images[0]
        
        # save calibration result to json
        self.save_quantized_model()

    def get_kl_divergence(self, module, input, output):
        for i, inp in enumerate(input):
            if inp is not None:
                if isinstance(inp, List): #ip adapter tensor maybe list
                    inp = inp[0]
                layer_name = module.__name__
                if "transformer_blocks" in layer_name and ("ff" in layer_name or "attn" in layer_name or "proj_mlp" in layer_name or "proj_out" in layer_name):
                    key_ = f"{layer_name}.input{i}.kl_div"
                    scale_ = self.all_act_range[f"{module.__name__}.input{i}.scale"][-1]
                    kl_div_value = compute_kl_divergence(quantize_tensor(inp, scale_), inp)
                    if key_ in self.all_kl_div.keys():
                        self.all_kl_div[key_].append(kl_div_value)
                    else:
                        self.all_kl_div[key_] = [kl_div_value]

    def get_activation_range(self, module, input, output):
        for i, inp in enumerate(input):
            if inp is not None:
                if isinstance(inp, List): #ip adapter tensor maybe list
                    inp = inp[0]

                layer_name = f"{module.__name__}.input{i}.maxmin"
                if "transformer_blocks" in layer_name and ("ff" in layer_name or "attn" in layer_name or "proj_mlp" in layer_name or "proj_out" in layer_name):

                    #calibration
                    cur_min, cur_max = get_maxmin_range(inp, self.args.calib_method)
                    if None == cur_min and None == cur_max: #use fp16 precision
                        pass
                    else:
                        if layer_name in self.all_act_range.keys():
                            pre_min, pre_max = self.all_act_range[layer_name]
                            cur_min = pre_min if pre_min<cur_min else cur_min
                            cur_max = pre_max if pre_max>cur_max else cur_max
                    self.all_act_range[layer_name] = [cur_min, cur_max]
                    self.all_act_range[f"{module.__name__}.input{i}.shape"] = inp.shape

                    #save output tensor value if to_q to_k or to_v, for attention fp8 qiantization
                    if "to_q" in layer_name or "to_k" in layer_name or "to_v" in layer_name:
                        key_name = f"{module.__name__}.output{i}.maxmin"
                        out_min, out_max = get_maxmin_range(output, self.args.calib_method)
                        if (None != out_min and None != out_max) and key_name in self.all_act_range.keys(): #need update the max-min range
                            pre_min, pre_max = self.all_act_range[key_name]
                            out_min = pre_min if pre_min<out_min else out_min
                            out_max = pre_max if pre_max>out_max else out_max
                        self.all_act_range[key_name] = [out_min, out_max]
                        self.all_act_range[f"{module.__name__}.output{i}.shape"] = output.shape
                else:
                    pass
        return
    def get_activation_range_controlnet(self, module, input, output):
        for i, inp in enumerate(input):
            if inp is not None:
                if isinstance(inp, List): #ip adapter tensor maybe list
                    inp = inp[0]

                layer_name = f"{module.__name__}.input{i}.maxmin"
                if "transformer_blocks" in layer_name and ("ff" in layer_name or "attn" in layer_name or "proj_mlp" in layer_name or "proj_out" in layer_name):

                    #calibration
                    cur_min, cur_max = get_maxmin_range(inp, self.args.calib_method)
                    if None == cur_min and None == cur_max: #use fp16 precision
                        pass
                    else:
                        if layer_name in self.all_act_range_controlnet.keys():
                            pre_min, pre_max = self.all_act_range_controlnet[layer_name]
                            cur_min = pre_min if pre_min<cur_min else cur_min
                            cur_max = pre_max if pre_max>cur_max else cur_max
                    self.all_act_range_controlnet[layer_name] = [cur_min, cur_max]
                    self.all_act_range_controlnet[f"{module.__name__}.input{i}.shape"] = inp.shape
                else:
                    pass
        return
    
    def save_quantized_model(self):
        if self.calculate_kl_divergence:
            self.dump_kl_divergence(self.args.dump_path)
        else:
            self.dump_act_scale(self.args.dump_path, self.all_act_range)
            if None != self.all_act_range_controlnet:
                self.dump_act_scale(self.args.dump_path.replace('.json', '_controlnet.json'), self.all_act_range_controlnet)

    def dump_kl_divergence(self, dump_path):
        kl_div_dict = {}

        #pick up transformer layer
        for k,v in self.all_kl_div.items():
            kl_div_dict[k] = torch.stack(v).cpu().numpy().tolist()
        
        # Serializing json
        json_object = json.dumps(kl_div_dict, indent=4)
        
        # Writing to sample.json
        with open(dump_path, "w") as outfile:
            outfile.write(json_object)

    def dump_act_scale(self, dump_path, all_act_range_dict):
        tensor_scale_dict = {}

        finfo = torch.finfo(torch.float8_e4m3fn)

        #pick up transformer layer
        for k,v in all_act_range_dict.items():
            if ".maxmin" in k and "transformer_blocks" in k and ("ff" in k or "attn" in k or "proj_mlp" in k or "proj_out" in k):
                key_ = k.replace('.maxmin', '.scale')
                if None == v[0] and None == v[1]:
                    tensor_scale_dict[key_] = [None, None, None]
                else:
                    amax = torch.maximum(v[0].abs(), v[1].abs()).clamp(min=1e-12)
                    scale = amax/finfo.max
                    tensor_scale_dict[key_] = [v[0].float().cpu().numpy().tolist(), v[1].float().cpu().numpy().tolist(), scale.float().cpu().numpy().tolist()]

                    #we support fp8-attention-quantization for debug, set the scale to 1.0
                    if ".output" in key_ and ("to_q" in key_ or "to_k" in key_ or "to_v" in key_):
                        tensor_scale_dict[key_] = [v[0].float().cpu().numpy().tolist(), v[1].float().cpu().numpy().tolist(), 1.0]
        
        # Serializing json
        json_object = json.dumps(tensor_scale_dict, indent=4)
        
        # Writing to sample.json
        with open(dump_path, "w") as outfile:
            outfile.write(json_object)

def read_act_scale(dump_path):
    with open(dump_path, "r") as read_file:
        data = json.load(read_file)
    return data
def compute_kl_divergence(input_, target_):
    '''
    The relation is:
    kl_divergence(p||q) = cross_entropy(p,q) - entropy(p)
    cross_entropy(p,q) = - sum(p * log(q))
    entropy(p) = - sum(p * log(p))
    kl_divergence(p||q) = sum(p * (log(p) - log(q))) = sum(p * log(p/q))
    
    Parameters:
    input_: tensor of shape (batch x seq_len, hidden_size)
    target_: tensor of shape (batch x seq_len, hidden_size)
    '''
    hidden_size = input_.size(-1)
    q = input_.view(-1, hidden_size).float()
    p = target_.view(-1, hidden_size).float()
    return torch.nn.functional.kl_div(q.softmax(-1).log(), p.softmax(-1), reduction='batchmean')

def quantize_tensor(tensor, scale):
    hidden_size = tensor.size(-1)
    fp8_tensor = to_float8(tensor.view(-1, hidden_size), put_scale=torch.tensor([scale], device=tensor.device))
    dequantize_tensor = fp8_tensor[0].to(tensor.dtype) * scale
    return dequantize_tensor

def hist_statistic_calib(tensor, bins = 100, threshold=0.999):
    '''
    find the proper max-min range with histogram
    '''
    amax = torch.maximum(tensor.min().abs(), tensor.max().abs()).clamp(min=1e-12)

    #debug: we don't use hist in the range of [-448, 448]
    if amax < 448.0:
        return -amax, amax

    hist_tensor = torch.histc(tensor.float(), bins=bins, min=-amax, max=amax)
    bin_width = (2*amax) / bins
    mid_index = bins // 2
    for i in range(mid_index):
        cur_hist = hist_tensor[(mid_index - 1 - i):(mid_index + i + 1)]
        cur_sum = cur_hist.sum()
        if cur_sum / hist_tensor.sum() > threshold:
            return -((i+1)*bin_width), (i+1)*bin_width
        
    return -amax, amax

def mixed_precision_calib(tensor, max_value=600.0):
    '''
    use mixed precision to calibrate the tensor, if the tensor amax is less than max_value, we use fp8-quantization, otherwise we use fp16-precision
    '''
    amax = torch.maximum(tensor.min().abs(), tensor.max().abs()).clamp(min=1e-12)

    if amax < max_value:
        return -amax, amax
    else:
        return None, None


def kl_divergence_calib(tensor, candidate_num=5):
    values, _ = tensor.flatten().topk(candidate_num, dim=0, largest=True, sorted=True)
    finfo = torch.finfo(torch.float8_e4m3fn)
    candidate_scale = values.abs()/finfo.max

    min_kl_div = float('inf')
    selected_idx = 0
    for i in range(candidate_num):
        kl_div_value = compute_kl_divergence(quantize_tensor(tensor, candidate_scale[i].float()), tensor)
        if kl_div_value < min_kl_div:
            min_kl_div = kl_div_value
            selected_idx = i
    
    return -values[selected_idx].abs(), values[selected_idx].abs()


def get_maxmin_range(tensor, method='max-min'):
    if 'max-min' == method:
        return tensor.aminmax()
    elif 'hist' == method:
        return hist_statistic_calib(tensor.flatten())
    elif 'mixed' == method:
        return mixed_precision_calib(tensor.flatten())
    else:
        return kl_divergence_calib(tensor)