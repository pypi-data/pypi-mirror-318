# Copyright 2024 the LlamaFactory team.
# Copyright (c) 2024 Huawei Technologies Co., Ltd.
#
# This code is inspired by the LLaMA-Factory.
# https://github.com/hiyouga/LLaMA-Factory/blob/main/src/src/llamafactory/data/processors/supervised.py
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

from openmind.archived.models.auto import AutoTokenizer
from openmind.utils import get_logger
from openmind.utils.constants import IGNORE_INDEX
from ..template import Template
from ...arguments import DatasetsArguments


logger = get_logger(__name__)  # pylint: disable=invalid-name


def _encode_supervised_example(
    prompt, response, system, tools, template: Template, tokenizer: AutoTokenizer, datasets_args: DatasetsArguments
):
    """
    Perform encode operation on the data of supervised_example.
    Returns:
        input_ids, labels
    """
    messages = prompt + response
    input_ids, labels = [], []

    encoded_pairs = template.encode(tokenizer, messages, datasets_args)
    for turn_idx, (source_ids, target_ids) in enumerate(encoded_pairs):
        # add source mask
        source_mask = [IGNORE_INDEX] * len(source_ids)
        input_ids += source_ids + target_ids
        labels += source_mask + target_ids

    return input_ids, labels


def preprocess_supervised_dataset(
    examples, template: Template, tokenizer: AutoTokenizer, datasets_args: DatasetsArguments
):
    """
    Used for processing supervised datasets.
    Args:
        examples: examples of datasets
        template: The template inherited from Template.
        tokenizer: Tokenizer
        datasets_args: arguments of datasets
    Returns:
        Processed data.
    """
    model_inputs = {"input_ids": [], "attention_mask": [], "labels": []}

    for i in range(len(examples["prompt"])):
        if len(examples["prompt"][i]) % 2 != 1 or len(examples["response"][i]) != 1:
            logger.warning("Dropped invalid example: {}".format(examples["prompt"][i] + examples["response"][i]))
            continue

        input_ids, labels = _encode_supervised_example(
            prompt=examples["prompt"][i],
            response=examples["response"][i],
            system=examples["system"][i],
            tools=examples["tools"][i],
            template=template,
            tokenizer=tokenizer,
            datasets_args=datasets_args,
        )
        model_inputs["input_ids"].append(input_ids)
        model_inputs["attention_mask"].append([1] * len(input_ids))
        model_inputs["labels"].append(labels)

    return model_inputs
