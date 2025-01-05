import argparse
import logging
import sys

from lmot.args import add_cli_args

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main(args):
    if args.sub_command == "llm-quant":
        # delayed import to avoid some unnecessary dependencies
        from lmot.quantize.awq import AWQQuant
        from lmot.quantize.gptq import GPTQQuant
        from lmot.quantize.smoothquant import SmoothQuant
        if args.quant_method == "gptq":
            gptq_obj = GPTQQuant(args)
            gptq_obj.gptq_quant()
        elif args.quant_method == "smooth-w8a8":
            smooth_obj = SmoothQuant(args)
            smooth_obj.smooth_quant()
        elif args.quant_method == "awq":
            awq_obj = AWQQuant(args)
            awq_obj.awq_quant()
        else:    
            raise NotImplementedError(f"quantization method {args.quant_method} is not implemented.")
    elif args.sub_command == "ldm-quant":
        # delayed import to avoid some unnecessary dependencies
        from lmot.quantize.ldm.ldm_quant import LDMQuantizer
        quantizer = LDMQuantizer.quantizer_factory(args)
        quantizer.model_quantize()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="LOT optimize pipeline", conflict_handler='resolve')
    args = add_cli_args(parser)
    logger.info(f"args: {args}")

    main(args)
