# Copyright (c) 2024 Huawei Technologies Co., Ltd.
# All rights reserved.
#
# openMind is licensed under Mulan PSL v2.
# You can use this software according to the terms and conditions of the Mulan PSL v2.
# You may obtain a copy of Mulan PSL v2 at:
#
#          http://license.coscl.org.cn/MulanPSL2
#
# THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND,
# EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT,
# MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
# See the Mulan PSL v2 for more details.

import importlib
import os
import argparse
import sys
import textwrap
from pathlib import Path

from tqdm import tqdm
from transformers import AutoModelForCausalLM
from .subcommand import SubCommand
from ..flow.model import get_tokenizer
from ..utils.logging import get_logger
from ..flow.model.loader import get_init_kwargs, get_config
from ..flow.arguments.parser import get_export_args
from ..flow.model.model_registry import register_builtin_models

logger = get_logger()


def lora_merge_and_unload(base_model: AutoModelForCausalLM, adapter_models: str):
    peft_module = importlib.import_module("peft")
    model = peft_module.PeftModel.from_pretrained(base_model, adapter_models)
    model = model.merge_and_unload()
    return model


def parse_input_to_list(input_string):
    input_string = input_string.strip()

    if input_string.startswith("[") and input_string.endswith("]"):
        input_string = input_string.replace("[", "").replace("]", "").strip()
    return input_string.split(",")


class Export(SubCommand):

    def __init__(self, subparsers: argparse._SubParsersAction):
        super().__init__()
        self._parser = subparsers.add_parser(
            "export",
            prog="openmind-cli export",
            help="merge finetuned adapter weight to base model",
            description="loading yaml file to start merge and export",
            epilog=textwrap.dedent(
                """\
            examples:
                $ openmind-cli export qwen2_7b_lora_merge.yaml 
                ...
            """
            ),
            formatter_class=argparse.RawTextHelpFormatter,
        )
        self._add_arguments()
        self._parser.set_defaults(func=self._export_cmd)

    def _export_cmd(self, args: argparse.Namespace):

        if os.path.isfile(sys.argv[-1]) and sys.argv[-1].endswith(".yaml"):
            yaml_file = sys.argv[-1]
        else:
            raise ValueError("Please provide valid yaml file path.")

        model_args, training_args = get_export_args(yaml_file)

        if model_args.adapter_models is None or training_args.output_dir is None:
            raise ValueError("Please set adapter_models and output path to start merge and export.")

        # create output_dir if it's not existed
        try:
            path_obj = Path(training_args.output_dir)
        except Exception as e:
            raise ValueError(f"The path {training_args.output_dir} is not a valid path format.") from e

        if not path_obj.exists():
            path_obj.mkdir(parents=True, exist_ok=True)
            logger.info(f"Directory {training_args.output_dir} is created for saving merge model")
        else:
            if any(os.scandir(training_args.output_dir)):
                raise ValueError(
                    "The output dir is not empty."
                    "Please select a empty folder avoiding cover existing model files."
                    "Or setting the output_dir param with a new folder name, the process will build it for you."
                )
            logger.info(f"Directory {training_args.output_dir} is used for saving merge model")

        adapter_model_list = parse_input_to_list(model_args.adapter_models)

        register_builtin_models()

        init_kwargs = get_init_kwargs(model_args)
        config = get_config(model_args)
        tokenizer = get_tokenizer(model_args)

        logger.info(f"Start loading model from {model_args.model_name_or_path}")
        model = AutoModelForCausalLM.from_pretrained(
            pretrained_model_name_or_path=model_args.model_name_or_path,
            config=config,
            torch_dtype=getattr(config, "torch_dtype", None),
            **init_kwargs,
        )

        logger.info("Start merging in cpu")

        for adapter in tqdm(adapter_model_list, desc="Merging adapters", unit="adapter"):
            model = lora_merge_and_unload(model, adapter)

        # if not set per_shard_size, the max_shar_size will default to 5GB
        max_shard_size = f"{model_args.per_shard_size}GB" if model_args.per_shard_size else "5GB"

        model.save_pretrained(
            save_directory=training_args.output_dir, max_shard_size=max_shard_size, safe_serialization=True
        )
        tokenizer.save_pretrained(training_args.output_dir)
        logger.info(f"Lora weight has been successfully merged to base model and saved in {training_args.output_dir}")
