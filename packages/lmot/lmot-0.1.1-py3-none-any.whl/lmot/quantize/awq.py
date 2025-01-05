import torch
import time
import logging
import os
from awq import AutoAWQForCausalLM
from transformers import AutoTokenizer
from lmot.quantize.common import BaseQuant

from llmcompressor.modifiers.quantization import GPTQModifier
from llmcompressor.modifiers.smoothquant import SmoothQuantModifier
from llmcompressor.transformers import oneshot
from lmot.quantize.common import BaseQuant

logger = logging.getLogger(__name__)

class AWQQuant(BaseQuant):
    def __init__(self, args):
        super().__init__(args)

    def awq_quant(self):
        if self.args.quant_bits == 8:
            logger.warning("AWQ only support 4-bit quantization, set quant_bits to 4")
            self.args.quant_bits = 4
        quant_config = { "zero_point": True, "q_group_size": 128, "w_bit": self.args.quant_bits, "version": "GEMM" }

        # Load model
        model = AutoAWQForCausalLM.from_pretrained(self.args.pretrained_model_dir)
        tokenizer = AutoTokenizer.from_pretrained(self.args.pretrained_model_dir, trust_remote_code=True)

        if self.args.dataset_type == "alpaca":
            examples = self.load_alpaca_data_autoawq(self.args.quant_dataset, tokenizer, self.args.n_samples)
            examples_for_quant = [
                {"input_ids": example["input_ids"], "attention_mask": example["attention_mask"]} for example in examples
            ]
        elif self.args.dataset_type == "sharegpt":
            examples_for_quant = self.load_sharegpt_data_autoawq(self.args.quant_dataset, tokenizer, self.args.n_samples)
        else:
            raise ValueError(f"dataset_type: {self.args.dataset_type} is not supported, currently only support [alpaca conversation].")

        # start quantization
        logger.info(f"{'='*10} start quantization {'='*10}")
        start = time.time()

        # Quantize
        model.quantize(tokenizer, quant_config=quant_config,calib_data=examples_for_quant)

        end = time.time()
        logger.info(f"quantization model took: {end - start: .4f}s")

        if not self.args.quantized_model_dir:
            self.args.quantized_model_dir = f"{self.args.pretrained_model_dir}-GPTQ{self.args.quant_bits}"

        # save quantized model
        logger.info(f"saving quantized model to {self.args.quantized_model_dir}")
        model.save_quantized(self.args.quantized_model_dir)
        
        # save tokenizer
        tokenizer.save_pretrained(self.args.quantized_model_dir)

