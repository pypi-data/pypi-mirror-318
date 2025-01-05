import json 
import jsonlines
import torch
import logging
from transformers import AutoConfig

from datasets import load_dataset, Dataset

logger = logging.getLogger(__name__)

class BaseQuant:
    def __init__(self, args):
        self.args = args
        if torch.cuda.is_available():
            self.device = "cuda"
        else:
            self.device = "cpu"
        self.hf_config = AutoConfig.from_pretrained(args.pretrained_model_dir)

    def alpaca_data_convert(self, ds, tokenizer):
        def tokenize(example):
            msg = [
                {"role": "user", "content": example["instruction"] + example["input"]},
                {"role": "assistant", "content": example["output"]}
            ]
            text = tokenizer.apply_chat_template(msg, tokenize=False, add_generation_prompt=False)
            tokenized_data = tokenizer(text)
            return {
                "input_ids": tokenized_data["input_ids"][: tokenizer.model_max_length],
                "attention_mask": tokenized_data["attention_mask"][: tokenizer.model_max_length],
            }
                
        ds = ds.map(tokenize, num_proc=8, keep_in_memory=True, load_from_cache_file=False)
        return ds
    
    def load_alpaca_data_llmcompressor(self, data_path, tokenizer, n_samples=512):
        # Load dataset and preprocess.
        ds = load_dataset(data_path)
        ds_split_size_max = 0
        quant_split_name = ""
        for k in ds.keys():
            if ds[k].num_rows > ds_split_size_max:
                ds_split_size_max = ds[k].num_rows
                quant_split_name = k
        ds = ds[quant_split_name]

        ds = ds.shuffle(seed=42).select(range(n_samples))
        
        def tokenize(example):
            msg = [
                {"role": "user", "content": example["instruction"] + example["input"]},
                {"role": "assistant", "content": example["output"]}
            ]
            text = tokenizer.apply_chat_template(msg, tokenize=False, add_generation_prompt=False)
            return tokenizer(
                text,
                padding=False,
                max_length=tokenizer.model_max_length,
                truncation=True,
                add_special_tokens=False,
            )
                
        ds = ds.map(tokenize, num_proc=8, keep_in_memory=True, load_from_cache_file=False)
        return ds

    def load_sharegpt_data_llmcompressor(self, data_path, tokenizer, n_samples=512):
        # Load dataset and preprocess.
        ds = load_dataset(data_path)
        ds_split_size_max = 0
        quant_split_name = ""
        for k in ds.keys():
            if ds[k].num_rows > ds_split_size_max:
                ds_split_size_max = ds[k].num_rows
                quant_split_name = k
        ds = ds[quant_split_name]

        ds = ds.shuffle(seed=42).select(range(n_samples))
        
        def tokenize(example):
            msg = []
            conv = example["conversations"]
            for i in range(0, len(conv), 2):
                if i + 1 < len(conv):
                    msg.extend([
                        {"role": "user", "content": conv[i]["value"]},
                        {"role": "assistant", "content": conv[i+1]["value"]}
                    ])
                else:
                    # 处理奇数情况，只有一个用户输入没有对应的助手回复
                    msg.append({"role": "user", "content": conv[i]["value"]})

            text = tokenizer.apply_chat_template(msg, tokenize=False, add_generation_prompt=False)
            return tokenizer(
                text,
                padding=False,
                max_length=tokenizer.model_max_length,
                truncation=True,
                add_special_tokens=False,
            )
                
        ds = ds.map(tokenize, num_proc=8, keep_in_memory=True, load_from_cache_file=False,remove_columns=ds.column_names)
        return ds

    def load_alpaca_data_autogptq(self, data_path, tokenizer):
        with open(data_path, "r", encoding="utf-8") as f:
            raw_data = json.load(f)

        # raw_data = random.sample(raw_data, k=min(n_samples, len(raw_data)))

        def dummy_gen():
            return raw_data

        def tokenize(examples):
            instructions = examples["instruction"]
            inputs = examples["input"]
            outputs = examples["output"]

            messages = []

            for istr, inp, opt in zip(instructions, inputs, outputs):
                msg =  [
                        {"role": "user", "content": istr + inp},
                        {"role": "assistant", "content": opt}
                    ]
                messages.append(msg)

            prompts = []
            texts = []
            input_ids = []
            attention_mask = []
            for msg in messages:
                text = tokenizer.apply_chat_template(msg, tokenize=False, add_generation_prompt=False)
                tokenized_data = tokenizer(text)
                input_ids.append(tokenized_data["input_ids"][: tokenizer.model_max_length])
                attention_mask.append(tokenized_data["attention_mask"][: tokenizer.model_max_length])

                prompts.append(text)
                texts.append(text)

            return {
                "input_ids": input_ids,
                "attention_mask": attention_mask,
            }

        dataset = Dataset.from_generator(dummy_gen)

        dataset = dataset.map(
            tokenize,
            batched=True,
            batch_size=len(dataset),
            num_proc=8,
            keep_in_memory=True,
            load_from_cache_file=False,
            remove_columns=["instruction", "input"],
        )

        dataset = dataset.to_list()

        for sample in dataset:
            sample["input_ids"] = torch.LongTensor(sample["input_ids"]).to(self.device)
            sample["attention_mask"] = torch.LongTensor(sample["attention_mask"]).to(self.device)

        return dataset
    
    def load_sharegpt_data_autogptq(self, data_path, tokenizer,n_samples):
        ds = load_dataset(data_path)
        ds_split_size_max = 0
        quant_split_name = ""
        for k in ds.keys():
            if ds[k].num_rows > ds_split_size_max:
                ds_split_size_max = ds[k].num_rows
                quant_split_name = k
        ds = ds[quant_split_name]

        ds = ds.shuffle(seed=42).select(range(n_samples))

        def tokenize(example):
            msg = []
            conv = example["conversations"]
            for i in range(0, len(conv), 2):
                if i + 1 < len(conv):
                    msg.extend([
                        {"role": "user", "content": conv[i]["value"]},
                        {"role": "assistant", "content": conv[i+1]["value"]}
                    ])
                else:
                    # 处理奇数情况，只有一个用户输入没有对应的助手回复
                    msg.append({"role": "user", "content": conv[i]["value"]})

            text = tokenizer.apply_chat_template(msg, tokenize=False, add_generation_prompt=False)
            return tokenizer(
                text,
                padding=False,
                max_length=tokenizer.model_max_length,
                truncation=True,
                add_special_tokens=False,
            )

        ds = ds.map(tokenize, num_proc=8, keep_in_memory=True, load_from_cache_file=False,remove_columns=ds.column_names)

        return ds

    def load_alpaca_data_autoawq(self, data_path, tokenizer, n_samples):
        # Load dataset and preprocess.
        ds = load_dataset(data_path)
        ds_split_size_max = 0
        quant_split_name = ""
        for k in ds.keys():
            if ds[k].num_rows > ds_split_size_max:
                ds_split_size_max = ds[k].num_rows
                quant_split_name = k
        ds = ds[quant_split_name]

        ds = ds.shuffle(seed=42).select(range(n_samples))

        dataset_list = []
        for d in ds:
            msg = [
                {"role": "user", "content": d["instruction"] + d["input"]},
                {"role": "assistant", "content": d["output"]}
            ]
            text = tokenizer.apply_chat_template(msg, tokenize=False, add_generation_prompt=False)
            dataset_list.append(text.strip())
        return dataset_list

    def load_sharegpt_data_autoawq(self, data_path, tokenizer, n_samples):
        ds = load_dataset(data_path)
        ds_split_size_max = 0
        quant_split_name = ""
        for k in ds.keys():
            if ds[k].num_rows > ds_split_size_max:
                ds_split_size_max = ds[k].num_rows
                quant_split_name = k
        ds = ds[quant_split_name]

        ds = ds.shuffle(seed=42).select(range(n_samples))

        datasets_list = []
        for d in ds:
            msg = []
            conv = d["conversations"]
            for i in range(0, len(conv), 2):
                if i + 1 < len(conv):
                    msg.extend([
                        {"role": "user", "content": conv[i]["value"]},
                        {"role": "assistant", "content": conv[i+1]["value"]}
                    ])
                else:
                    # 处理奇数情况，只有一个用户输入没有对应的助手回复
                    msg.append({"role": "user", "content": conv[i]["value"]})

            text = tokenizer.apply_chat_template(msg, tokenize=False, add_generation_prompt=False)
            datasets_list.append(text.strip())
        return datasets_list

    def load_conversation_data(self, data_path, tokenizer):
        dataset = []
        with jsonlines.open(data_path) as reader:
            for obj in reader:
                dataset.append(obj)

        data = []
        for msg in dataset:
            text = tokenizer.apply_chat_template(msg, tokenize=False, add_generation_prompt=False)
            model_inputs = tokenizer([text])
            input_ids = torch.tensor(model_inputs.input_ids[:4096], dtype=torch.int)
            data.append(dict(input_ids=input_ids, attention_mask=input_ids.ne(tokenizer.pad_token_id)))
        return data
