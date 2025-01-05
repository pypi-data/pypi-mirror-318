import argparse

def add_cli_args(parser: argparse.ArgumentParser):
    subparsers = parser.add_subparsers(dest='sub_command', help='sub-command help')

    # llm quantization args
    parser_quantization = subparsers.add_parser('llm-quant', help='llm model quantization')
    parser_quantization.add_argument(
        "--pretrained-model-dir", 
        type=str, 
        required=True,
        default=None,
        help="The directory of the pretrained model."
    )

    parser_quantization.add_argument(
        "--quantized-model-dir", 
        type=str, 
        default=None,
        help="The directory to save the quantized model.")
    
    parser_quantization.add_argument(
        "--quant-method",
        type=str,
        default="gptq",
        choices=[
            "awq",
            "gptq",
            "smooth-w8a8"
        ],
        help="The quantization method.",
    )
    parser_quantization.add_argument(
        "--quant-bits",
        type=int,
        default=8,
        choices=[2, 4, 8],
        help="The number of bits to quantize to.",
    )
    parser_quantization.add_argument(
        "--quant-dataset",
        type=str,
        default=None,
        help="The dataset to use for quantization.",
    )
    parser_quantization.add_argument(
        "--dataset-type", 
        type=str, 
        default="sharegpt", 
        choices=["alpaca", "sharegpt"],
        help="The type of dataset to use for quantization."
    )
    parser_quantization.add_argument(
        "--group-size",
        type=int,
        default=128,
        help="group size, -1 means no grouping or full rank",
    )
    parser_quantization.add_argument(
        "--desc-act", 
        action="store_true", 
        help="whether to quantize with desc_act"
    )
    
    parser_quantization.add_argument(
        "--quant-batch-size",
        type=int,
        default=1,
        help="The batch size to use for quantization.",
    )

    parser_quantization.add_argument(
        "--n-samples",
        type=int,
        default=512,
        help="The number of samples to use for quantization.",
    )

    # ldm quantization args
    parser_ldm_quantization = subparsers.add_parser('ldm-quant', help='ldm model quantization')
    parser_ldm_quantization.add_argument(
        "--result-format",
        type=str,
        required=True,
        choices=["json","weight"],
        help="The format of the quantization result, json or weight. json: save the scale to json file, weight: save the quantized weight and activation in new model."
    )
    parser_ldm_quantization.add_argument(
        "--model-path",
        type=str,
        required=True,
        default=None,
        help="The directory of the pretrained model."
    )
    parser_ldm_quantization.add_argument(
        "--model-architecture",
        type=str,
        required=True,
        choices=["sdxl","sdxl-controlnet","flux"],
        help="The architecture of the model."
    )
    parser_ldm_quantization.add_argument(
        "--calib-method",
        type=str,
        default="max-min",
        choices=["max-min","mixed","hist","kl-diverg"],
        help="The calibration algorithm: max-min/mixed-precision/histogram/kl-divergence."
    )
    parser_ldm_quantization.add_argument(
        "--quanted-model-dir",
        type=str,
        default=None,
        help="The directory to save the quantized model."
    )
    parser_ldm_quantization.add_argument(
        "--controlnet-model-path",
        type=str,
        default=None,
        help="The directory of the controlnet model."
    )
    parser_ldm_quantization.add_argument(
        "--vae-model-path",
        type=str,
        default=None,
        help="The directory of the vae model."
    )
    parser_ldm_quantization.add_argument(
        "--controlnet-image-path",
        type=str,
        default=None,
        help="The path of the image."
    )
    parser_ldm_quantization.add_argument(
        "--ipadapter-model-path",
        type=str,
        default=None,
        help="The path of the ipadapter model."
    )
    parser_ldm_quantization.add_argument(
        "--ipadapter-model-subfolder",
        type=str,
        default=None,
        help="The subfolder of the ipadapter model."
    )
    parser_ldm_quantization.add_argument(
        "--ipadapter-weight-name",
        type=str,
        default=None,
        help="The weight name of the ipadapter model."
    )
    parser_ldm_quantization.add_argument(
        "--ipadapter-scale",
        type=float,
        default=0.6,
        help="The scale of the ipadapter model inference."
    )
    parser_ldm_quantization.add_argument(
        "--ipadapter-image-path",
        type=str,
        default=None,
        help="The path of the ipadapter image."
    )
    parser_ldm_quantization.add_argument(
        "--prompts",
        type=str,
        default="A photo of a cat",
        help="The prompt to use for generate picture."
    )
    parser_ldm_quantization.add_argument(
        "--negative-prompts",
        type=str,
        default=None,
        help="The negative prompt to use for generate picture."
    )
    parser_ldm_quantization.add_argument(
        "--steps",
        type=int,
        default=25,
        help="The number of steps to use for generate picture."
    )
    parser_ldm_quantization.add_argument(
        "--width",
        type=int,
        default=512,
        help="The width of the picture."
    )
    parser_ldm_quantization.add_argument(
        "--height",
        type=int,
        default=512,
        help="The height of the picture."
    )

    parser_ldm_quantization.add_argument(
        "--quant-method",
        type=str,
        default="fp8",
        choices=["fp8","w4a4"],
        help="The quantization method."
    )
    parser_ldm_quantization.add_argument(
        "--seed",
        type=int,
        default=42,
        help="The seed to use for generate picture."
    )
    parser_ldm_quantization.add_argument(
        "--dump-path",
        type=str,
        default=None,
        help="The path to save scale josn, it will be used for online inference."
    )
    parser_ldm_quantization.add_argument(
        "--act-range-file",
        type=str,
        default=None,
        help="The path to the activation range file."
    )
    return parser.parse_args()

