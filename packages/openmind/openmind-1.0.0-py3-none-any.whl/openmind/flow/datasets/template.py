# Copyright 2024 the LlamaFactory team.
# Copyright (c) 2024 Huawei Technologies Co., Ltd.
#
# This code is inspired by the LLaMA-Factory.
# https://github.com/hiyouga/LLaMA-Factory/blob/main/src/llamafactory/data/template.py
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

import json
from pathlib import Path
from typing import Dict, List

from ..arguments import DatasetsArguments


TEMPLATES: Dict[str, "Template"] = {}


# Adapted from https://github.com/hiyouga/LLaMA-Factory/blob/f2b2a37f0819bb344998a9059c02b97ca5a5ae74/src/llamafactory/data/template.py#L39
class Template:
    def __init__(
        self,
        system_template: str = "",
        user_template: str = "",
        assistant_template: str = "",
        separator_template: str = "{content}",
        default_system: str = "",
        force_use_system: bool = True,
        replace_eos: bool = False,
    ):
        self.system_template = system_template
        self.user_template = user_template
        self.assistant_template = assistant_template
        self.separator_template = separator_template
        self.default_system = default_system
        self.force_use_system = force_use_system
        self.replace_eos = replace_eos

    def _convert_elements_to_ids(self, tokenizer, elements: List[str], add_eos_token: bool):
        token_ids = []
        for elem in elements:
            if isinstance(elem, str):
                if len(elem) != 0:
                    token_ids += tokenizer.encode(elem, add_special_tokens=False)
                if add_eos_token:
                    token_ids += [tokenizer.eos_token_id]
            else:
                raise ValueError("Input must be string, got {}".format(type(elem)))

        return token_ids

    def _infer_max_len(self, source_len: int, target_len: int, max_len: int, reserved_label_len: int):
        # The target length is obtained by taking a length in proportion from the remaining maximum length.
        max_target_len = int(max_len * (target_len / (source_len + target_len)))
        # If a minimum reserved length is specified, then take the larger value.
        max_target_len = max(max_target_len, reserved_label_len)
        # The source takes the remaining length.
        max_source_len = max_len - min(max_target_len, target_len)
        return max_source_len, max_target_len

    def _make_pairs(self, encoded_messages: List[List[int]], cutoff_len: int, reserved_label_len: int):
        """
        Used to turn it into a pair of question and answer.
        """
        encoded_pairs = []
        total_length = 0
        for i in range(0, len(encoded_messages), 2):
            if total_length >= cutoff_len:
                break

            max_source_len, max_target_len = self._infer_max_len(
                source_len=len(encoded_messages[i]),
                target_len=len(encoded_messages[i + 1]),
                max_len=(cutoff_len - total_length),
                reserved_label_len=reserved_label_len,
            )
            source_ids = encoded_messages[i][:max_source_len]
            target_ids = encoded_messages[i + 1][:max_target_len]
            total_length += len(source_ids) + len(target_ids)
            encoded_pairs.append((source_ids, target_ids))

        return encoded_pairs

    def encode(self, tokenizer, messages: List[Dict[str, str]], datasets_args: DatasetsArguments, **kwargs):
        encoded_messages = []
        for i, message in enumerate(messages):
            elements = []
            add_eos_token = False
            if i == 0 and self.force_use_system:
                elements.append(self.system_template.format_map({"content": self.default_system}))
            elif i > 0 and i % 2 == 0:
                # Question and answer. The order is user and assistant in turn.
                # Therefore, a separator needs to be added every two items.
                elements.append(self.separator_template.format_map(message))
            if message["role"] == "user":
                elements.append(self.user_template.format_map(message))
            elif message["role"] == "assistant":
                elements.append(self.assistant_template.format_map(message))
                add_eos_token = True
            else:
                raise NotImplementedError("Unexpected role: {}".format(message["role"]))
            # start encoding operations here.
            encoded_messages.append(self._convert_elements_to_ids(tokenizer, elements, add_eos_token))

        return self._make_pairs(encoded_messages, datasets_args.cutoff_len, datasets_args.reserved_label_len)


def register_template(
    name: str,
    system_template: str = "",
    user_template: str = "",
    assistant_template: str = "",
    separator_template: str = "",
    default_system: str = "",
):
    r"""
    Registers a chat template.
    """
    TEMPLATES[name] = Template(
        system_template=system_template,
        user_template=user_template,
        assistant_template=assistant_template,
        separator_template=separator_template,
        default_system=default_system,
    )


def register_builtin_templates():
    r"""
    Registers all builtin chat templates.
    """
    template_config_path = Path(__file__).resolve().parent.parent / "configs/templates.json"
    with open(template_config_path, "r", encoding="utf-8") as f:
        config = json.load(f)
    templates_dict = {template["name"]: template for template in config}

    for name, config in templates_dict.items():
        register_template(
            name=name,
            system_template=config.get("system_template", ""),
            user_template=config.get("user_template", ""),
            assistant_template=config.get("assistant_template", ""),
            separator_template=config.get("separator_template", ""),
            default_system=config.get("default_system", "You are a helpful assistant."),
        )


# Make sure the function is executed only once.
register_builtin_templates()


def get_template(name: str):
    return TEMPLATES[name]
