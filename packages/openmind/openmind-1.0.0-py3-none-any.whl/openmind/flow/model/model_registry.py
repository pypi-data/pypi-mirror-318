# Copyright (c) 2024 Huawei Technologies Co., Ltd.
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

import json
from dataclasses import dataclass
from collections import OrderedDict
from typing import Dict, Optional
from pathlib import Path

from ..arguments import ModelArguments


# "Qwen2-0.5B":
SUPPORTED_MODELS = OrderedDict()
# "qwen2":
SUPPORTED_MODEL_GROUPS = OrderedDict()


@dataclass
class ModelGroupMetadata:
    lora_target: str
    template: str


@dataclass
class ModelMetadata:
    lora_target: str
    template: str
    path: Dict[str, str]


def register_model_group(
    model_group: str,
    models: Dict[str, Dict[str, str]],
    lora_target: str = None,
    template: Optional[str] = None,
) -> None:
    """
    Register a model group with the given models

    Args:
        model_group (str): Name of the model group.
        models (Dict[str, Dict[str, str]]): A dict of models, where the key is the model name and the value is the model path.
        lora_target (str, optional): Names of layers to insert LoRA weights. Defaults to None.
        template (Optional[str], optional): The prompt template of the model group. Defaults to None.
    """
    SUPPORTED_MODEL_GROUPS[model_group] = ModelGroupMetadata(lora_target, template)
    for name, path in models.items():
        SUPPORTED_MODELS[name] = ModelMetadata(lora_target, template, path)


def register_builtin_models():
    """
    Registers all builtin models which are predefined in 'configs/models.json'.
    """
    models_path = Path(__file__).resolve().parent.parent / "configs/models.json"
    with open(models_path, "r", encoding="utf-8") as f:
        config = json.load(f)

    for model_group, model_item in config.items():
        register_model_group(
            model_group=model_group,
            models=model_item["models"],
            lora_target=model_item.get("lora_target"),
            template=model_item.get("template"),
        )


register_builtin_models()


def get_template_type(model_args: ModelArguments) -> str:
    """
    Return the prompt template type from the parsed given model arguments

    Args:
        model_args (ModelArguments): The model arguments.

    Returns:
        str: The prompt template type.
    """
    if model_args.model_id is not None:
        template_type = SUPPORTED_MODELS[model_args.model_id].template
    else:
        template_type = SUPPORTED_MODEL_GROUPS[model_args.model_group].template
    return template_type


def get_model_lora_target(model_args: ModelArguments) -> str:
    """
    Return a list of layers to insert LoRA weights

    Args:
        model_args (ModelArguments): The model arguments.

    Returns:
        str: A list of layers to insert LoRA weights. The layers are seperated by commas.
    """
    if model_args.model_id is not None:
        lora_target = SUPPORTED_MODELS[model_args.model_id].lora_target
    else:
        lora_target = SUPPORTED_MODEL_GROUPS[model_args.model_group].lora_target
    return [target.strip() for target in lora_target.split(",")]
