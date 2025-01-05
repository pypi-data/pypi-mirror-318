import torch
import logging
import json
from lmot.quantize.ldm.ldm_quant import LDMQuantizer
from lmot.quantize.ldm.utils import to_float8

logger = logging.getLogger(__name__)

class UnetQuantizer(LDMQuantizer):
    def __init__(self, args):
        super().__init__(args)
        self.all_act_range = {}
        self.transformer_act_range = {}

    def model_quantize(self):
        unet_model_state_dict = self.pipe.unet.state_dict()

        # qkv fusion
        fused_qkv_model = self.mm_fusion(unet_model_state_dict)
        
        # weight quantization
        quantized_weight_model = self.weight_quant(fused_qkv_model)

        # activation quantization
        self.get_activation_quant_scale()
        quantized_activation_model = self.activation_quant(quantized_weight_model)

        # save quantized model
        quanted_model_dir = f"{self.args.quanted_model_dir}-unet"
        self.save_quantized_model(quantized_activation_model, quanted_model_dir)
        
    def mm_fusion(self, model):
        """
        Optimize the fusion of weights in the model by reducing redundant operations and improving memory usage.
        """

        def fuse_weights(base_key, model):
            # Fuse q, k, v weights for attn1
            qkv_weights = [model[f"{base_key}.attn1.to_q.weight"],
                        model[f"{base_key}.attn1.to_k.weight"],
                        model[f"{base_key}.attn1.to_v.weight"]]
            model[f"{base_key}.attn1.qkv_weight"] = torch.cat(qkv_weights, dim=1).transpose(0, 1).contiguous()
            del model[f"{base_key}.attn1.to_q.weight"]
            del model[f"{base_key}.attn1.to_k.weight"]
            del model[f"{base_key}.attn1.to_v.weight"]

            # Fuse k, v weights for attn2
            kv_weights = [model[f"{base_key}.attn2.to_k.weight"],
                        model[f"{base_key}.attn2.to_v.weight"]]
            model[f"{base_key}.attn2.kv_weight"] = torch.cat(kv_weights, dim=1).transpose(0, 1).contiguous()
            del model[f"{base_key}.attn2.to_k.weight"]
            del model[f"{base_key}.attn2.to_v.weight"]

        # Process down blocks
        # blocks 1 and 2, 2 transformer blocks for 0 down block, 10 transformer blocks for 1 down block, 2 attention blocks for each down block
        for m in range(1, 3):
            transformer_block_num = 2 if m == 1 else 10
            for i in range(2):
                for j in range(transformer_block_num):
                    base_key = f"down_blocks.{m}.attentions.{i}.transformer_blocks.{j}"
                    fuse_weights(base_key, model)

        # Process mid block
        # 1 mid block, 1 attention block, 10 transformer blocks
        for m in range(1):
            for i in range(1):
                for j in range(10):
                    base_key = f"mid_block.attentions.{i}.transformer_blocks.{j}"
                    fuse_weights(base_key, model)

        # Process up blocks
        # 3 up blocks, 3 attention blocks for 0,1 up block, 0 attention blocks for 2 up block
        # 10 transformer blocks for 0 up block, 2 transformer blocks for 1 up block, 0 transformer blocks for 2 up block
        for m in range(3):
            attention_block_num = 0 if m == 2 else 3
            transformer_block_num = 10 if m == 0 else (2 if m == 1 else 0)
            for i in range(attention_block_num):
                for j in range(transformer_block_num):
                    base_key = f"up_blocks.{m}.attentions.{i}.transformer_blocks.{j}"
                    fuse_weights(base_key, model)

        torch.cuda.empty_cache()
        return model

    def weight_quant(self, model, quant_type=torch.float8_e4m3fn):
        """
        SDXL unet model weight quantization. Only for feed-forward and attention layers.
        """
        def quantize_weights(base_key, model, quant_type):
            # feed-forward
            model[f"{base_key}.ff.proj1_weight"], model[f"{base_key}.ff.proj1_quant_scale"] = to_float8(
                model[f"{base_key}.ff.net.0.proj.weight"], dtype=quant_type)
            model[f"{base_key}.ff.proj2_weight"], model[f"{base_key}.ff.proj2_quant_scale"] = to_float8(
                model[f"{base_key}.ff.net.2.weight"], dtype=quant_type)
            # attention
            model[f"{base_key}.attn1.qkv_weight"], model[f"{base_key}.attn1.qkv_quant_scale"] = to_float8(
                model[f"{base_key}.attn1.qkv_weight"], dtype=quant_type)
            model[f"{base_key}.attn1.out_weight"], model[f"{base_key}.attn1.out_quant_scale"] = to_float8(
                model[f"{base_key}.attn1.to_out.0.weight"], dtype=quant_type)
            model[f"{base_key}.attn2.q_weight"], model[f"{base_key}.attn2.q_quant_scale"] = to_float8(
                model[f"{base_key}.attn2.to_q.weight"], dtype=quant_type)
            model[f"{base_key}.attn2.kv_weight"], model[f"{base_key}.attn2.kv_quant_scale"] = to_float8(
                model[f"{base_key}.attn2.kv_weight"], dtype=quant_type)
            model[f"{base_key}.attn2.out_weight"], model[f"{base_key}.attn2.out_quant_scale"] = to_float8(
                model[f"{base_key}.attn2.to_out.0.weight"], dtype=quant_type)

        # down blocks
        for m in range(1, 3):
            transformer_block_num = 2 if m == 1 else 10
            for i in range(2):
                for j in range(transformer_block_num):
                    base_key = f"down_blocks.{m}.attentions.{i}.transformer_blocks.{j}"
                    quantize_weights(base_key, model, quant_type)

        # mid block
        for i in range(1):
            for j in range(10):
                base_key = f"mid_block.attentions.{i}.transformer_blocks.{j}"
                quantize_weights(base_key, model, quant_type)

        # up blocks
        for m in range(3):
            attention_block_num = 0 if m == 2 else 3
            transformer_block_num = 10 if m == 0 else (2 if m == 1 else 0)
            for i in range(attention_block_num):
                for j in range(transformer_block_num):
                    base_key = f"up_blocks.{m}.attentions.{i}.transformer_blocks.{j}"
                    quantize_weights(base_key, model, quant_type)

        torch.cuda.empty_cache()
        return model
    
    def activation_quant(self, model):
        
        def quantize_activation(base_key, model):
            device_type = model[f'{base_key}.ff.proj1_quant_scale'].device
            #feed-forward
            model[f'{base_key}.ff.proj1_input_scale'] = self.transformer_act_range[f'{base_key}.ff.net.0.input0.scale']
            model[f'{base_key}.ff.proj2_input_scale'] = self.transformer_act_range[f'{base_key}.ff.net.2.input0.scale']
            #attention
            model[f'{base_key}.attn1.qkv_input_scale'] = self.transformer_act_range[f'{base_key}.attn1.to_q.input0.scale']
            model[f'{base_key}.attn1.out_input_scale'] = self.transformer_act_range[f'{base_key}.attn1.to_out.0.input0.scale']
            model[f'{base_key}.attn2.q_input_scale'] = self.transformer_act_range[f'{base_key}.attn2.to_q.input0.scale']
            model[f'{base_key}.attn2.kv_input_scale'] = self.transformer_act_range[f'{base_key}.attn2.to_k.input0.scale']
            model[f'{base_key}.attn2.out_input_scale'] = self.transformer_act_range[f'{base_key}.attn2.to_out.0.input0.scale']
        
        # down blocks
        for m in range(1, 3):
            transformer_block_num = 2 if m == 1 else 10
            for i in range(2):
                for j in range(transformer_block_num):
                    base_key = f"down_blocks.{m}.attentions.{i}.transformer_blocks.{j}"
                    quantize_activation(base_key, model)
        
        # mid block
        for i in range(1):
            for j in range(10):
                base_key = f"mid_block.attentions.{i}.transformer_blocks.{j}"
                quantize_activation(base_key, model)
        
        # up blocks
        for m in range(3):
            attention_block_num = 0 if m == 2 else 3
            transformer_block_num = 10 if m == 0 else (2 if m == 1 else 0)
            for i in range(attention_block_num):
                for j in range(transformer_block_num):
                    base_key = f"up_blocks.{m}.attentions.{i}.transformer_blocks.{j}"
                    quantize_activation(base_key, model)

        torch.cuda.empty_cache()
        return model
    
    def get_activation_quant_scale(self):
        hooked_model = self.pipe.unet        
        # Register a hook for each layer
        for name, layer in hooked_model.named_modules():
            layer.__name__ = name
            layer.register_forward_hook(self.get_activation_range)

        gen = torch.Generator().manual_seed(self.args.seed)
        images = self.pipe(prompt=self.args.prompts, num_inference_steps=self.args.steps, generator=gen, width=self.args.width, height=self.args.height).images[0]
        
        #pick up transformer layer
        finfo = torch.finfo(torch.float8_e4m3fn)
        for k,v in self.all_act_range.items():
            if ".maxmin" in k and "transformer_blocks" in k and ("ff" in k or "attn" in k or "proj_mlp" in k or "proj_out" in k):
                amax = torch.maximum(v[0].abs(), v[1].abs()).clamp(min=1e-12)
                scale = amax/finfo.max
                key_ = k.replace('.maxmin', '.scale')
                self.transformer_act_range[key_] = scale
        return
    
    def get_activation_range(self, module, input, output):
        for i, inp in enumerate(input):
            if inp is not None:
                cur_min, cur_max = inp.aminmax()
                layer_name = f"{module.__name__}.input{i}.maxmin"
                if layer_name in self.all_act_range.keys():
                    pre_min, pre_max = self.all_act_range[layer_name]
                    cur_min = pre_min if pre_min<cur_min else cur_min
                    cur_max = pre_max if pre_max>cur_max else cur_max
                self.all_act_range[layer_name] = [cur_min, cur_max]
                self.all_act_range[f"{module.__name__}.input{i}.shape"] = inp.shape
        return