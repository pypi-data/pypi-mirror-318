from llmcompressor.modifiers.quantization import GPTQModifier
from llmcompressor.modifiers.smoothquant import SmoothQuantModifier
from llmcompressor.transformers import oneshot
from transformers import AutoModelForCausalLM
import os
os.environ["CUDA_LAUNCH_BLOCKING"] = "1"
# Select quantization algorithm. In this case, we:
#   * apply SmoothQuant to make the activations easier to quantize
#   * quantize the weights to int8 with GPTQ (static per channel)
#   * quantize the activations to int8 (dynamic per token)
recipe = [
    SmoothQuantModifier(smoothing_strength=0.8),
    GPTQModifier(scheme="W8A8", targets="Linear", ignore=["lm_head"]),
]
model = AutoModelForCausalLM.from_pretrained(
    "/data1/nfs15/nfs/bigdata/zhanglei/ml/inference/model-demo/hf/TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    trust_remote_code=True,
    device_map="auto",
    torch_dtype="auto",
)
# Apply quantization using the built in open_platypus dataset.
#   * See examples for demos showing how to pass a custom calibration set
oneshot(
    # model="/data1/nfs15/nfs/bigdata/zhanglei/ml/inference/model-demo/hf/TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    model=model,
    dataset="open_platypus",
    recipe=recipe,
    output_dir="TinyLlama-1.1B-Chat-v1.0-INT8",
    max_seq_length=2048,
    num_calibration_samples=10,
)
model.save_pretrained("TinyLlama-1.1B-Chat-v1.0-INT8-test", save_compressed=True, safe_serialization=True)
# tokenizer.save_pretrained("TinyLlama-1.1B-Chat-v1.0-INT8")

# CUDA_VISIBLE_DEVICES=0,1,2,3 python test.py
# python optimize.py quantization --pretrained-model-dir /data1/nfs15/nfs/bigdata/zhanglei/ml/inference/model-demo/hf/Qwen/Qwen2.5-7B-Instruct --quant-dataset /data1/nfs15/nfs/bigdata/zhanglei/ml/datasets/shibing624/alpaca-zh --dataset-type alpaca