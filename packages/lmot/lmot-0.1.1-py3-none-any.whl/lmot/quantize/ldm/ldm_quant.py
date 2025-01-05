import torch
import logging
import os
from diffusers import DiffusionPipeline,ControlNetModel,StableDiffusionXLControlNetPipeline,AutoencoderKL
from safetensors.torch import save_file

logger = logging.getLogger(__name__)

class LDMQuantizer:
    def __init__(self, args):
        self.args = args
        # check args
        self.check_args()
        # load diffusers pipeline
        if torch.cuda.is_available():
            self.device = "cuda"
        self.pipe = self.load_pipeline()

    @classmethod
    def quantizer_factory(cls, args):
        if args.result_format == "json":
            logger.info(f"Get model activation range to a json file.")
            from lmot.quantize.ldm.ldm_calib import LDMCalibrator
            return LDMCalibrator(args)
        else:
            if args.model_architecture == "sdxl":
                logger.info(f"Quant unet model for sdxl model.")
                from lmot.quantize.ldm.unet_quant import UnetQuantizer
                return UnetQuantizer(args)
            elif args.model_architecture == "sdxl-controlnet":
                logger.info(f"Quant controlnet model for sdxl-controlnet model.")
                from lmot.quantize.ldm.controlnet_quant import ControlNetQuantizer
                return ControlNetQuantizer(args)
            else:
                raise NotImplementedError(f"quantization method {args.model_architecture} is not implemented.")
        
    def load_pipeline(self):
        if self.args.model_architecture == "sdxl-controlnet":
            controlnet_model = ControlNetModel.from_pretrained(self.args.controlnet_model_path, torch_dtype=torch.float16)
            vae = AutoencoderKL.from_pretrained(self.args.vae_model_path, torch_dtype=torch.float16)
            pipe = StableDiffusionXLControlNetPipeline.from_pretrained(
                self.args.model_path,
                controlnet=controlnet_model,
                vae=vae,
                torch_dtype=torch.float16,
            )
        else:
            pipe = DiffusionPipeline.from_pretrained(self.args.model_path, torch_dtype=torch.float16)
            if self.args.ipadapter_model_path is not None:
                logger.info(f"Load ipadapter model from {self.args.ipadapter_model_path}")
                pipe.load_ip_adapter(self.args.ipadapter_model_path, 
                                            subfolder = self.args.ipadapter_model_subfolder,
                                            weight_name = self.args.ipadapter_weight_name)
                pipe.set_ip_adapter_scale(self.args.ipadapter_scale)
        return pipe.to(self.device)
    
    def model_quantize(self):
        pass
    
    def check_args(self):
        if self.args.model_architecture == "sdxl-controlnet":
            assert self.args.controlnet_model_path is not None, "controlnet_model_path should be provided."
            assert self.args.vae_model_path is not None, "vae_model_path should be provided."
            assert self.args.controlnet_image_path is not None, "controlnet_image_path should be provided."
        if self.args.quanted_model_dir is None:
            self.args.quanted_model_dir = f"{self.args.model_path}-{self.args.quant_method}"
        
        if self.args.ipadapter_model_path is not None:
            assert self.args.ipadapter_image_path is not None, "ipadapter_image_path should be provided."
            assert self.args.ipadapter_model_subfolder is not None, "ipadapter_model_subfolder should be provided."
            assert self.args.ipadapter_weight_name is not None, "ipadapter_weight_name should be provided."

        if self.args.result_format == "json":
            logger.warning(f"Model will be calibrated with {self.args.calib_method}, you may choose best method to calibrate model.")
            if self.args.dump_path is None and self.args.ipadapter_model_path is not None:
                self.args.dump_path = f"{self.args.model_architecture}-ipadapter-{self.args.calib_method}.json"
            elif self.args.dump_path is None and self.args.model_architecture == "sdxl-controlnet":
                self.args.dump_path = f"sdxl-{self.args.calib_method}.json"
            else:
                self.args.dump_path = f"{self.args.model_architecture}-{self.args.calib_method}.json"

    def save_quantized_model(self, quantized_model, save_dir):
        # create no exist dir
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        save_file(quantized_model, f'{save_dir}/model_weights.safetensors')

            
 