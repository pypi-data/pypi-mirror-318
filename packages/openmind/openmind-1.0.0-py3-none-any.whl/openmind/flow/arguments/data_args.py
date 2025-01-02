# Copyright (c) 2024 Huawei Technologies Co., Ltd.
# Copyright 2024 the LlamaFactory team.
#
# Adapt some arguments from llamafactory
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

from dataclasses import dataclass, field
from typing import Optional

from openmind.utils import get_logger


logger = get_logger(__name__)


@dataclass
class DatasetsArguments:
    dataset: Optional[str] = field(default=None, metadata={"help": "The name of the dataset."})
    custom_dataset_info: Optional[str] = field(
        default=None,
        metadata={"help": "The absoluted path of the customized json file, externally inputting by the user."},
    )
    subset_name: Optional[str] = field(
        default=None,
        metadata={
            "help": "Name of the sub dataset in the dataset. When it is necessary to specify the download"
            " of one of multiple sub datasets."
        },
    )
    split: Optional[str] = field(
        default="train",
        metadata={
            "help": "Load a subset of the partitioned dataset, such as' train '. If the value is None, "
            "it will return all the data included."
        },
    )
    preprocessing_num_workers: Optional[int] = field(
        default=None, metadata={"help": "The number of processes to use for the data processing."}
    )
    preprocessing_batch_size: int = field(
        default=1000,
        metadata={"help": "The number of examples in one group in pre-processing."},
    )
    cutoff_len: int = field(
        default=1024,
        metadata={"help": "The cutoff length of the tokenized inputs in the dataset."},
    )
    max_length: Optional[int] = field(
        default=None,
        metadata={
            "help": "Pad to a maximum length specified with the argument `max_length`. If `cutoff_len` "
            "is set, the maximum length equal to `max(cutoff_len, max_length)`"
        },
    )
    reserved_label_len: int = field(
        default=1,
        metadata={"help": "The minimum cutoff length reserved for the tokenized labels in the dataset."},
    )
    ignore_pad_token_for_loss: bool = field(
        default=True,
        metadata={"help": "Whether or not to ignore the tokens corresponding to the pad label in loss computation."},
    )

    def __post_init__(self):
        if self.max_length is not None:
            if self.max_length < self.cutoff_len:
                logger.warning_rank0(
                    f"Set max_length to {self.cutoff_len} to ensure it meets or exceeds the value of cutoff_len."
                )
                self.max_length = self.cutoff_len
