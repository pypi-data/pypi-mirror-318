# Copyright 2024 the LlamaFactory team.
# Copyright (c) 2024 Huawei Technologies Co., Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# Adapted from https://github.com/hiyouga/LLaMA-Factory/blob/7965e9840c18c71028c1a3a04c404e9fae196c0d/src/llamafactory/model/loader.py#L53

import os

import torch

import transformers
from transformers import (
    AutoConfig,
    AutoTokenizer,
    AutoModelForCausalLM,
    BitsAndBytesConfig,
    Seq2SeqTrainingArguments,
)
from transformers.dynamic_module_utils import get_relative_imports

from openmind.utils import logging
from ..arguments import FinetuneArguments, ModelArguments
from .model_registry import SUPPORTED_MODELS
from .adapter import apply_adapter


logger = logging.get_logger(__name__)  # pylint: disable=invalid-name


def try_download_from_hub(model_args: ModelArguments) -> str:
    if os.path.exists(model_args.model_name_or_path):
        return model_args.model_name_or_path

    # download from modelers
    from openmind.utils.hub import snapshot_download

    return snapshot_download(
        model_args.model_name_or_path,
        revision=model_args.model_revision,
        cache_dir=model_args.cache_dir,
        token=model_args.token,
    )


def skip_check_imports() -> None:
    r"""
    Avoids flash attention import error in custom model files.
    """
    if os.environ.get("FORCE_CHECK_IMPORTS", "0").lower() not in ["true", "1"]:
        transformers.dynamic_module_utils.check_imports = get_relative_imports


def get_init_kwargs(model_args: ModelArguments):
    skip_check_imports()
    if model_args.model_id is not None and model_args.model_name_or_path is None:
        model_args.model_name_or_path = SUPPORTED_MODELS[model_args.model_id].path["modelers"]

    model_args.model_name_or_path = try_download_from_hub(model_args)

    return {
        "trust_remote_code": model_args.trust_remote_code,
        "cache_dir": model_args.cache_dir,
        "revision": model_args.model_revision,
    }


def get_config(model_args: ModelArguments):
    r"""
    Load model config.
    NB: May change attributes in model_args
    """
    init_kwargs = get_init_kwargs(model_args)
    config = AutoConfig.from_pretrained(model_args.model_name_or_path, **init_kwargs)

    # model_group is deprecated, the model_type is temporarily assigned to model_group
    if not (model_args.model_id or model_args.model_group):
        model_args.model_group = config.model_type

    return config


def get_tokenizer(model_args: ModelArguments):
    r"""
    Load pretrained tokenizer.
    """
    init_kwargs = get_init_kwargs(model_args)
    try:
        tokenizer = AutoTokenizer.from_pretrained(
            model_args.model_name_or_path,
            use_fast=model_args.use_fast_tokenizer,
            split_special_tokens=model_args.split_special_tokens,
            padding_size="right",
            **init_kwargs,
        )
    except ValueError:
        # try the fast version
        tokenizer = AutoTokenizer.from_pretrained(
            model_args.model_name_or_path,
            use_fast=True,
            padding_side="right",
            **init_kwargs,
        )
    except Exception as e:
        raise RuntimeError("Failed to load tokenizer.") from e

    if model_args.new_special_tokens is not None:
        num_added_tokens = tokenizer.add_special_tokens(
            dict(additional_special_tokens=model_args.new_special_tokens),
            replace_additional_special_tokens=False,
        )
        logger.info_rank0(
            "Add special tokens: {}, num_added_tokens: {}".format(
                ",".join(model_args.special_tokens_dict.keys()), num_added_tokens
            )
        )
        if num_added_tokens > 0 and not model_args.resize_vocab:
            model_args.resize_vocab = True
            logger.warning_rank0("New tokens have been added, changed `resize_vocab` to True.")

    return tokenizer


def get_model(
    model_args: ModelArguments,
    finetune_args: FinetuneArguments,
    training_args: Seq2SeqTrainingArguments,
):
    r"""
    Loads pretrained model.
    """
    init_kwargs = get_init_kwargs(model_args)
    config = get_config(model_args)

    if model_args.load_in_4bit:
        if not training_args.bf16:
            raise ValueError("we only support bnb_4bit_compute_dtype=bf16")
        nf4_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.bfloat16,
        )
    else:
        nf4_config = None

    model = AutoModelForCausalLM.from_pretrained(
        pretrained_model_name_or_path=model_args.model_name_or_path,
        config=config,
        quantization_config=nf4_config,
        torch_dtype=torch.bfloat16 if training_args.bf16 else "auto",
        **init_kwargs,
    )

    model = apply_adapter(model, model_args, finetune_args, training_args.do_train)

    if training_args.do_train:
        model.train()

        if model_args.use_gradient_checkpointing and model.supports_gradient_checkpointing:
            model.gradient_checkpointing_enable()
            logger.info_rank0("Gradient checkpointing has been enabled.")
    else:
        model.eval()

    return model
