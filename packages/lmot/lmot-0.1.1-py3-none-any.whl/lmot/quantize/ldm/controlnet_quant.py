import torch
from lmot.quantize.ldm.ldm_quant import LDMQuantizer
from lmot.quantize.ldm.utils import to_float8
from lmot.args import Args

class ControlNetQuantizer(LDMQuantizer):
    def __init__(self, args:Args):
        super().__init__(args)
        self.all_act_range = {}