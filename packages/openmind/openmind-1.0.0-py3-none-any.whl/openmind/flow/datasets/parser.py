# Copyright (c) 2024 Huawei Technologies Co., Ltd.
# Copyright 2024 the LlamaFactory team.
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

from dataclasses import dataclass
from typing import Any, Dict, Optional, Literal

from openmind.utils.constants import DATASET_INFO_CONFIG


@dataclass
class InstructionDatasetAttr:
    r"""
    Dataset attributes for standard instruction dataset.
    """

    # basic configs
    name: Optional[str] = None
    load_from: Optional[str] = "om_hub"
    file_name: Optional[str] = None
    formatting: Literal["alpaca", "sharegpt"] = "alpaca"
    ranking: bool = False
    # extra configs
    subset: Optional[str] = None
    split: str = "train"
    folder: Optional[str] = None
    num_samples: Optional[int] = None
    # common columns
    system: Optional[str] = None
    tools: Optional[str] = None
    # alpaca columns
    prompt: Optional[str] = "instruction"
    query: Optional[str] = "input"
    response: Optional[str] = "output"
    history: Optional[str] = None
    # sharegpt columns
    messages: Optional[str] = "conversations"
    # sharegpt tags
    role_tag: Optional[str] = "from"
    content_tag: Optional[str] = "value"
    user_tag: Optional[str] = "human"
    assistant_tag: Optional[str] = "gpt"
    observation_tag: Optional[str] = "observation"
    function_tag: Optional[str] = "function_call"
    system_tag: Optional[str] = "system"

    def set_attr(self, key: str, obj: Dict[str, Any], default: Optional[Any] = None) -> None:
        setattr(self, key, obj.get(key, default))


def get_dataset_list(dataset: Optional[str], dataset_info) -> "InstructionDatasetAttr":
    r"""
    Gets the attributes of the datasets.
    """

    if dataset not in dataset_info:
        raise ValueError("Undefined dataset {} in {}.".format(dataset, DATASET_INFO_CONFIG))

    if "hub_url" in dataset_info[dataset]:
        local_from = dataset_info[dataset]["hub_url"]
    elif "local_path" in dataset_info[dataset]:
        local_from = dataset_info[dataset]["local_path"]
    else:
        raise ValueError(
            "Please provide local_path parameter in custom_dataset_info.json file when loading the local or custom dataset."
        )

    dataset_attr = InstructionDatasetAttr(name=dataset, load_from=local_from)

    if "file_name" in dataset_info[dataset]:
        dataset_attr.set_attr("file_name", dataset_info[dataset], default=None)

    dataset_attr.set_attr("formatting", dataset_info[dataset], default="alpaca")
    dataset_attr.set_attr("subset", dataset_info[dataset])
    dataset_attr.set_attr("split", dataset_info[dataset], default="train")
    dataset_attr.set_attr("folder", dataset_info[dataset])
    dataset_attr.set_attr("num_samples", dataset_info[dataset])

    if "columns" in dataset_info[dataset]:
        column_names = ["system", "tools"]
        if dataset_attr.formatting == "alpaca":
            column_names.extend(["prompt", "query", "response", "history"])
        else:
            column_names.extend(["messages"])

        for column_name in column_names:
            dataset_attr.set_attr(column_name, dataset_info[dataset]["columns"])

    if dataset_attr.formatting == "sharegpt" and "tags" in dataset_info[dataset]:
        tag_names = (
            "role_tag",
            "content_tag",
            "user_tag",
            "assistant_tag",
            "observation_tag",
            "function_tag",
            "system_tag",
        )
        for tag in tag_names:
            dataset_attr.set_attr(tag, dataset_info[dataset]["tags"])

    return dataset_attr
