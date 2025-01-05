import torch
import time
import logging
import os
import shutil
from auto_gptq import AutoGPTQForCausalLM, BaseQuantizeConfig
from transformers import AutoTokenizer, AutoModelForCausalLM
from lmot.quantize.common import BaseQuant

from llmcompressor.modifiers.quantization import GPTQModifier
from llmcompressor.modifiers.smoothquant import SmoothQuantModifier
from llmcompressor.transformers import oneshot
from lmot.quantize.common import BaseQuant
from lmot.quantize.utils import copy_end_with_str_files, safe_make_dir
from torch.nn import functional as F

logger = logging.getLogger(__name__)

class GPTQQuant(BaseQuant):
    def __init__(self, args):
        super().__init__(args)

    def gptq_quant(self):
        if self.hf_config.model_type =="qwen2" and self.hf_config.num_hidden_layers==28:
            logger.info("f quant qwen2 7B model with llmcompressor_gptq")
            self.llmcompressor_gptq_quant()
        else:
            self.auto_gptq_quant()
            
    def auto_gptq_quant(self):
        # For qwen2.5-72B, FNN intermediate_size is 29568, it divided by 128 (group size) is 231,
        # when inference with tensor patallel, head size and weight shape must be divisible by tp_size,
        # so the quanted model with group_size 128 only can be used with tp_size=1.

        # Func padding_weight will padding weight shape to 29696
        need_padding = (self.hf_config.model_type =="qwen2" and self.hf_config.num_hidden_layers==80)
        if need_padding:
            logger.warning("Padding weight shape to 29696 for qwen2 72B model")
            self.padding_weight()

        max_memory = {}
        if torch.cuda.is_available():
            gpu_properties = torch.cuda.get_device_properties(0)
            device_count = torch.cuda.device_count() if torch.cuda.device_count()==1 else torch.cuda.device_count() - 1
            max_memory.update({i: f"{(gpu_properties.total_memory / 1024**3)*0.85}GIB" for i in range(device_count)})

        # if max_memory:
        #     max_memory["cpu"] = f"{40}GIB"
        if not max_memory:
            max_memory = None
        logger.info(f"set quantize max_memory to : {max_memory}")

        tokenizer = AutoTokenizer.from_pretrained(
            self.args.pretrained_model_dir,
            use_fast=True,
            trust_remote_code=True,
        )
        quantize_config = BaseQuantizeConfig(
            bits=self.args.quant_bits, # 4 or 8
            group_size=self.args.group_size,
            damp_percent=0.01,
            desc_act=self.args.desc_act,  # set to False can significantly speed up inference but the perplexity may slightly bad
            static_groups=False,
            sym=True,
            true_sequential=True,
            model_name_or_path=None,
            model_file_base_name="model"
        )
        model = AutoGPTQForCausalLM.from_pretrained(
            self.args.pretrained_model_dir,
            quantize_config=quantize_config,
            max_memory=max_memory,
            trust_remote_code=True,
        )

        if self.args.dataset_type == "alpaca":
            examples = self.load_alpaca_data_autogptq(self.args.quant_dataset, tokenizer)
            examples_for_quant = [
                {"input_ids": example["input_ids"], "attention_mask": example["attention_mask"]} for example in examples
            ]
        elif self.args.dataset_type == "sharegpt":
            examples_for_quant = self.load_sharegpt_data_autogptq(self.args.quant_dataset, tokenizer, self.args.n_samples)
        else:
            raise ValueError(f"dataset_type: {self.args.dataset_type} is not supported, currently only support [alpaca conversation].")

        # start quantization
        logger.info(f"{'='*10} start quantization {'='*10}")
        start = time.time()

        model.quantize(
            examples_for_quant,
            batch_size=self.args.quant_batch_size,
            use_triton=False,
            autotune_warmup_after_quantized=True,
        )
        end = time.time()
        logger.info(f"quantization model took: {end - start: .4f}s")

        if not self.args.quantized_model_dir:
            self.args.quantized_model_dir = f"{self.args.pretrained_model_dir}-GPTQ{self.args.quant_bits}"

        # save quantized model
        logger.info(f"saving quantized model to {self.args.quantized_model_dir}")
        model.save_quantized(self.args.quantized_model_dir)
        # save tokenizer
        tokenizer.save_pretrained(self.args.quantized_model_dir)

        # delete tmp file
        if need_padding:
            shutil.rmtree(self.args.pretrained_model_dir)
        

    def padding_weight(self):
        # must use AutoModelForCausalLM
        model = AutoModelForCausalLM.from_pretrained(self.args.pretrained_model_dir,
                                                    torch_dtype="auto",device_map="auto")
        
        padding_model_path = f"{self.args.pretrained_model_dir}-padding"
        safe_make_dir(padding_model_path)

        # this size is Qwen2.5-72B only
        pad_size = 128
        sd = model.state_dict()

        for i, k in enumerate(sd):
            v = sd[k]
            # interleaving the padded zeros
            if ('mlp.up_proj.weight' in k) or ('mlp.gate_proj.weight' in k):
                prev_v = F.pad(v.unsqueeze(1), (0, 0, 0, 1, 0, 0)).reshape(29568*2, -1)[:pad_size*2]
                new_v = torch.cat([prev_v, v[pad_size:]], dim=0)
                sd[k] = new_v
            elif 'mlp.down_proj.weight' in k:
                prev_v= F.pad(v.unsqueeze(2), (0, 1)).reshape(8192, 29568*2)[:, :pad_size*2]
                new_v = torch.cat([prev_v, v[:, pad_size:]], dim=1)
                sd[k] = new_v
        # this is a very large file; make sure your RAM is enough to load the model
        torch.save(sd, f'{padding_model_path}/pytorch_model.bin')

        # save config
        self.hf_config.intermediate_size=29696
        self.hf_config.save_pretrained(padding_model_path)
        
        # copy other config files
        copy_end_with_str_files(".txt", self.args.pretrained_model_dir, padding_model_path)
        copy_end_with_str_files(".json", self.args.pretrained_model_dir, padding_model_path)

        # delete model.safetensors.index.json
        os.remove(f"{padding_model_path}/model.safetensors.index.json")

        # release memory
        del model
        torch.cuda.empty_cache()

        self.args.pretrained_model_dir = padding_model_path


    def llmcompressor_gptq_quant(self):
        tokenizer = AutoTokenizer.from_pretrained(self.args.pretrained_model_dir, use_fast=True, trust_remote_code=True)

        if self.args.dataset_type == "alpaca":
            tokenized_ds = self.load_alpaca_data_llmcompressor(self.args.quant_dataset, tokenizer, self.args.n_samples)
        elif self.args.dataset_type == "sharegpt":
            tokenized_ds = self.load_sharegpt_data_llmcompressor(self.args.quant_dataset, tokenizer, self.args.n_samples)
        else:
            raise NotImplementedError(f"Dataset type {self.args.dataset_type} not implemented.")
        
        # Configure the quantization algorithm to run.
        if self.args.quant_bits == 8:
            scheme = "W8A16"
        elif self.args.quant_bits == 4:
            scheme = "W4A16"
        else:
            raise ValueError(f"quant_bits: {self.args.quant_bits} is not supported, gptq currently only support [4, 8].")
        
        recipe = GPTQModifier(targets="Linear", scheme=scheme, ignore=["lm_head"], dampening_frac=0.1)

        # Apply algorithms and save to output_dir
        if not self.args.quantized_model_dir:
            self.args.quantized_model_dir = f"{self.args.pretrained_model_dir}-GPTQ{self.args.quant_bits}"
        logger.info(f"{'='*10} start quantization {'='*10}")
        start_time = time.time()
        oneshot(
            # model=self.args.pretrained_model_dir,
            model = self.args.pretrained_model_dir,
            # oneshot_device="cuda",
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
