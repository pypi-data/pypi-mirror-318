from lmot.quantize.ldm.ldm_quant import LDMQuantizer
from lmot.quantize.ldm.unet_quant import UnetQuantizer
import diffusers
from lmot.args import add_cli_args
import argparse
parser = argparse.ArgumentParser(description="LOT optimize pipeline", conflict_handler='resolve')

args = add_cli_args(parser)
print(args)
args.model_path = "/data1/nfs15/nfs/bigdata/zhanglei/ml/inference/model-demo/hf/stabilityai/stable-diffusion-xl-base-1.0"
args.model_architecture = "sdxl"

ldm_quantizer = LDMQuantizer.quantizer_factory(args)
ldm_quantizer.model_quantize()
#  = UnetQuantizer(args)
# ldm_quantizer.unet_optimize()

#  python -m lmot.optimize ldm-quant --model-path /data1/nfs15/nfs/bigdata/zhanglei/ml/inference/model-demo/hf/stabilityai/stable-diffusion-xl-base-1.0 --model-architecture sdxl