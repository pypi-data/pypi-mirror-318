from transformers.models.llama.configuration_llama import LlamaConfig
class EConfig(LlamaConfig):
    model_type = "llama"
    keys_to_ignore_at_inference = ["past_key_values"]