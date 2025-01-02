# Copyright 2024 the LlamaFactory team.
# Copyright (c) 2024 Huawei Technologies Co., Ltd.
#
# This code is inspired by the LLaMA-Factory.
# https://github.com/hiyouga/LLaMA-Factory/blob/main/src/llamafactory/data/aligner.py
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

from typing import TypedDict, List, Optional
from functools import partial

from datasets import concatenate_datasets
from transformers import Seq2SeqTrainingArguments

from ..parser import InstructionDatasetAttr
from ...arguments import DatasetsArguments


class ConversionOutput(TypedDict):
    prompt: List[List[dict]]
    response: List[List[dict]]
    system: List[List[dict]]
    tools: List[List[dict]]


def convert_alpaca(examples, datasets_attr: InstructionDatasetAttr, convert_system=False, convert_tools=False):
    """
    Convert the dataset to alpaca format.
    Args:
        examples: examples of datasets
        datasets_attr: The attributes of datasets.
        convert_system: Whether to convert system.
        convert_tools: Whether to convert tools.

    Returns:
        Output after conversion.
    """
    outputs: ConversionOutput = {"prompt": [], "response": [], "system": [], "tools": []}

    # TODO (#9) Currently, image input is not supported
    # TODO (#10) Currently, the row names are hard-coded. In the future, they should be read through JSON.
    for i in range(len(examples["instruction"])):
        # TODO (#11) Historical data needs to be added.
        prompt = []
        content = []

        if "history" in examples:
            if examples[datasets_attr.history][i] and isinstance(examples[datasets_attr.history][i], list):
                for history_item in examples[datasets_attr.history][i]:
                    prompt.append({"role": "user", "content": history_item[0]})
                    prompt.append({"role": "assistant", "content": history_item[1]})

        if examples[datasets_attr.prompt][i]:
            content.append(examples[datasets_attr.prompt][i])

        if examples[datasets_attr.query][i]:
            content.append(examples[datasets_attr.query][i])

        prompt.append({"role": "user", "content": "\n".join(content)})
        if isinstance(examples[datasets_attr.response][i], str):
            response = [{"role": "assistant", "content": examples[datasets_attr.response][i]}]
        else:  # unsupervised
            response = []

        outputs["prompt"].append(prompt)
        outputs["response"].append(response)
        outputs["system"].append(examples[datasets_attr.system][i] if convert_system else "")
        outputs["tools"].append(examples[datasets_attr.tools][i] if convert_tools else "")

    return outputs


def convert_sharegpt(examples, datasets_attr: InstructionDatasetAttr, convert_system=False, convert_tools=False):
    r"""
    Converts sharegpt format dataset to the standard format.
    Args:
        examples: examples of datasets
        datasets_attr: The attributes of datasets.
        convert_system: Whether to convert system.
        convert_tools: Whether to convert tools.

    Returns:
        Output after conversion.
    """
    outputs: ConversionOutput = {"prompt": [], "response": [], "system": [], "tools": []}
    value_map = {
        datasets_attr.user_tag: "user",
        datasets_attr.assistant_tag: "assistant",
        datasets_attr.observation_tag: "observation",
        datasets_attr.function_tag: "function",
        datasets_attr.system_tag: "system",
    }
    odd_tags = (datasets_attr.user_tag, datasets_attr.observation_tag)
    eve_tags = (datasets_attr.assistant_tag, datasets_attr.function_tag)
    accept_tags = (odd_tags, eve_tags)

    invalid_data = False

    # convert data
    conversations = examples[datasets_attr.messages]
    for conversation_list in conversations:
        messages = []
        prompt = []
        response = []
        for index, conversation in enumerate(conversation_list):
            if conversation[datasets_attr.role_tag] not in accept_tags[index % 2]:
                invalid_data = True

            prompt_converted = {
                "role": value_map[conversation[datasets_attr.role_tag]],
                "content": conversation[datasets_attr.content_tag],
            }
            messages.append(prompt_converted)
            prompt.append(prompt_converted)

        # check length
        if len(messages) % 2 != 0:
            invalid_data = True

        # convert prompt, response
        if not invalid_data:
            prompt = messages[:-1]
            response = messages[-1:]

        outputs["prompt"].append(prompt)
        outputs["response"].append(response)

    # convert system
    for i in range(len(examples[datasets_attr.messages])):
        outputs["system"].append(examples[datasets_attr.system_tag][i] if convert_system else "")
        outputs["tools"].append(examples[datasets_attr.tools][i] if convert_tools else "")

    return outputs


def align_dataset(
    dataset_attr: InstructionDatasetAttr,
    dataset,
    datasets_args: DatasetsArguments,
    training_args: Seq2SeqTrainingArguments,
):
    """
    In the align function, the format of the dataset is fixed.
    A field named "context" is added for the application of the template.
    Args:
        dataset: The dataset to be aligned.
        datasets_args: arguments of datasets

    Returns:
        The dataset after alignment.
    """
    # TODO (#8) Support datasets in other formats such as sharegpt.
    if dataset_attr.formatting == "alpaca":
        convert_func = partial(
            convert_alpaca,
            datasets_attr=dataset_attr,
            convert_system=True if "system" in dataset.column_names else False,
            convert_tools=True if "tools" in dataset.column_names else False,
        )
    elif dataset_attr.formatting == "sharegpt":
        convert_func = partial(
            convert_sharegpt,
            datasets_attr=dataset_attr,
            convert_system=True if "system" in dataset.column_names else False,
            convert_tools=True if "tools" in dataset.column_names else False,
        )
    else:
        raise ValueError("Data set formats are currently supported only by Alpaca and sharegpt")

    # The following code is consistent with the format of datasets in llama factory.
    column_names = list(next(iter(dataset)).keys())

    kwargs = dict(
        num_proc=datasets_args.preprocessing_num_workers,
        load_from_cache_file=training_args.local_process_index != 0,
        desc=f"Convert {dataset_attr.formatting} format dataset {dataset_attr.name} to standard format.",
    )
    return dataset.map(
        convert_func,
        batched=True,
        batch_size=datasets_args.preprocessing_batch_size,
        remove_columns=column_names,
        **kwargs,
    )


def merge_datasets(aligned_datasets: Optional[List[str]]):
    # TODO: How to pass seed/data_seed into _merge_dataset
    # TODO: Need to deal with the dataset in different cases (stf, rm...)
    if len(aligned_datasets) == 1:
        return aligned_datasets[0]
    else:
        return concatenate_datasets(aligned_datasets)
