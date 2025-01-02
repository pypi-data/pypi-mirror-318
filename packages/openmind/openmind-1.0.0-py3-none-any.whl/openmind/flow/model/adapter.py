# Copyright 2024 the LlamaFactory team.
# Copyright (c) 2024 Huawei Technologies Co., Ltd.
#
# This code is inspired by the LLaMA-Factory.
# https://github.com/hiyouga/LLaMA-Factory/blob/main/src/llamafactory/model/adapter.py
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

from typing import List

import torch
from transformers import PreTrainedModel
from peft import LoraConfig, TaskType, get_peft_model

from openmind.utils import logging
from ..arguments import FinetuneArguments, ModelArguments
from .model_registry import get_model_lora_target


logger = logging.get_logger(__name__)  # pylint: disable=invalid-name


def get_all_lora_target_modules(model) -> List[str]:

    remove_modules = ["lm_head"]

    lora_modules = {
        name.split(".")[-1]
        for name, module in model.named_modules()
        if not any(remove_module in name for remove_module in remove_modules)
        and "Linear" in module.__class__.__name__
        and "Embedding" not in module.__class__.__name__
    }

    return list(lora_modules)


def apply_lora(model, model_args: ModelArguments, finetune_args: FinetuneArguments):
    """
    Add lora through get_peft_model.
    Args:
        model: The model to which lora needs to be added.
        finetune_args: finetune_args: Parameters related to fine-tuning.
        model_group_name: group name of the model, get the corresponding lora configuration through model_group_name.

    Returns:
        The model after adding lora.
    """
    lora_target = get_model_lora_target(model_args)
    all_target_modules = get_all_lora_target_modules(model)
    if finetune_args.lora_target_modules == "all":
        target_modules = all_target_modules
    elif lora_target and not finetune_args.lora_target_modules:
        # this applys to registered model group wrapper with lora_target and user does not set any input lora target_info
        target_modules = lora_target
    elif finetune_args.lora_target_modules:
        # check whether input modules useful or not
        input_target_modules = set(finetune_args.lora_target_modules.replace(" ", "").split(","))
        if input_target_modules.issubset(all_target_modules):
            target_modules = input_target_modules
        else:
            raise ValueError(
                f"The input lora modules {input_target_modules} is not supported. The possible lora modules list is {all_target_modules}"
            )
    logger.info_rank0(f"Lora target modeules {target_modules} are applied to model")

    peft_kwargs = {
        "r": finetune_args.lora_rank,
        "target_modules": target_modules,
        "lora_alpha": finetune_args.lora_alpha if finetune_args.lora_alpha is not None else finetune_args.lora_rank * 2,
        "lora_dropout": finetune_args.lora_dropout,
    }

    lora_config = LoraConfig(
        task_type=TaskType.CAUSAL_LM,
        inference_mode=False,
        **peft_kwargs,
    )

    # According to: https://github.com/huggingface/peft/issues/137
    if model_args.use_gradient_checkpointing and model.supports_gradient_checkpointing:
        model.enable_input_require_grads()

    model = get_peft_model(model, lora_config)
    model.print_trainable_parameters()

    # Cast trainable parameters to fp32. According to the source code of PEFT, it has an improvement in stability.
    for param in filter(lambda p: p.requires_grad, model.parameters()):
        param.data = param.data.to(torch.float32)
    logger.debug("Cast parameters to fp32")
    return model


def apply_full(
    model,
    is_trainable: bool,
) -> None:
    if not is_trainable:
        return
    for param in model.parameters():
        param.data = param.data.to(torch.float32)


def apply_adapter(
    model: PreTrainedModel,
    model_args: ModelArguments,
    finetune_args: FinetuneArguments,
    is_trainable: bool,
) -> "PreTrainedModel":
    r"""
    Apply the adapters for LoRA training.

    Note that the trainable parameters must be cast to float32.(?)
    """
    if is_trainable and getattr(model, "quantization_method", None) is not None:
        if finetune_args.finetuning_type != "lora":
            raise ValueError("Quantized models can only be used for the LoRA tuning.")

    logger.info_rank0(f"Fine-tuning method: {finetune_args.finetuning_type}")
    if finetune_args.finetuning_type == "full":
        apply_full(model, is_trainable)
    elif finetune_args.finetuning_type == "lora":
        model = apply_lora(model, model_args, finetune_args)
    else:
        raise NotImplementedError(f"Unknown finetuning type: {finetune_args.finetuning_type}.")

    return model
