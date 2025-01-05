
import logging
import time
import os 
from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer

from llmcompressor.modifiers.quantization import GPTQModifier
from llmcompressor.modifiers.smoothquant import SmoothQuantModifier
from llmcompressor.transformers import oneshot
from lmot.quantize.common import BaseQuant

logger = logging.getLogger(__name__)
os.environ["CUDA_LAUNCH_BLOCKING"] = "1"

class SmoothQuant(BaseQuant):
    def __init__(self, args):
        super().__init__(args)

    def smooth_quant(self):
        # Select model and load it.
        # model = AutoModelForCausalLM.from_pretrained(
        #     self.args.pretrained_model_dir, 
        #     trust_remote_code=True,
        #     device_map="auto",
        #     torch_dtype="auto",
        # )
        tokenizer = AutoTokenizer.from_pretrained(self.args.pretrained_model_dir, use_fast=True, trust_remote_code=True)

        if self.args.dataset_type == "alpaca":
            tokenized_ds = self.load_alpaca_data_llmcompressor(self.args.quant_dataset, tokenizer, self.args.n_samples)
        elif self.args.dataset_type == "sharegpt":
            tokenized_ds = self.load_sharegpt_data_llmcompressor(self.args.quant_dataset, tokenizer, self.args.n_samples)
        else:
            raise NotImplementedError(f"Dataset type {self.args.dataset_type} not implemented.")
        
        # Configure algorithms. In this case, we:
        #   * apply SmoothQuant to make the activations easier to quantize
        #   * quantize the weights to int8 with GPTQ (static per channel)
        #   * quantize the activations to int8 (dynamic per token)
        recipe = [
            SmoothQuantModifier(smoothing_strength=0.8),
            GPTQModifier(targets="Linear", scheme="W8A8", ignore=["lm_head"]),
        ]

        # Apply algorithms and save to output_dir
        if not self.args.quantized_model_dir:
            self.args.quantized_model_dir = f"{self.args.pretrained_model_dir}-w8a8"
        logger.info(f"{'='*10} start quantization {'='*10}")
        start_time = time.time()
        oneshot(
            model=self.args.pretrained_model_dir,
            dataset=tokenized_ds,
            recipe=recipe,
            output_dir=self.args.quantized_model_dir,
            max_seq_length=tokenizer.model_max_length,
            num_calibration_samples=self.args.n_samples,
        )
        logger.info(f"quantization model took: {time.time() - start_time: .4f}s")

        # save quantized model
        # logger.info(f"saving quantized model to {self.args.quantized_model_dir}")
        # model.save_pretrained(self.args.quantized_model_dir, save_compressed=True)
        # tokenizer.save_pretrained(self.args.quantized_model_dir)
