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

import transformers
from openmind.utils import logging
from openmind.utils.import_utils import _is_package_available


logger = logging.get_logger(__name__)  # pylint: disable=invalid-name


@dataclass
class ModelArguments:
    model_id: str = field(
        default=None,
        metadata={
            "help": "Used to specify the id for the model, such as 'telechat-7b-pt', 'llama3-7b-chat'. "
            "If this parameter is not specified, try to query the registered template through model_name_or_path. "
            "If neither is available, use the common model template."
        },
    )
    model_group: str = field(
        default=None,
        metadata={"help": "Used to group of the model, such as 'qwen2', 'llama'. "},
    )
    model_name_or_path: str = field(
        default=None,
        metadata={
            "help": "The local path of the model or its name in the hub, "
            "such as /home/models/Telechat-7B-pt or TeleAI/Telechat-7B-pt"
        },
    )
    load_in_4bit: bool = field(default=False, metadata={"help": "Support for QLoRA, load the model in 4bits precision"})
    trust_remote_code: Optional[bool] = field(
        default=False,
        metadata={
            "help": (
                "Whether to trust the execution of code from datasets/models defined on the Hub."
                " This option should only be set to `True` for repositories you trust and in which you have read the"
                " code, as it will execute code present on the Hub on your local machine."
            )
        },
    )
    cache_dir: Optional[str] = field(default=None, metadata={"help": "Cache directory of downloaded models"})
    model_revision: str = field(
        default="main",
        metadata={"help": "The specific model version to use (can be a branch name, tag name or commit id)."},
    )
    use_fast_tokenizer: bool = field(
        default=True,
        metadata={"help": "Whether or not to use one of the fast tokenizer (backed by the tokenizers library)."},
    )
    split_special_tokens: bool = field(
        default=False,
        metadata={"help": "Whether or not the special tokens should be split during the tokenization process."},
    )
    new_special_tokens: Optional[str] = field(
        default=None,
        metadata={"help": "Special tokens to be added into the tokenizer. Use commas to separate multiple tokens."},
    )
    resize_vocab: bool = field(
        default=False,
        metadata={"help": "Whether or not to resize the tokenizer vocab."},
    )
    use_gradient_checkpointing: bool = field(
        default=True,
        metadata={"help": "Whether or not to use gradient checkpointing."},
    )
    adapter_models: str = field(
        default=None,
        metadata={"help": "The list of the adapter model to use."},
    )
    per_shard_size: int = field(
        default=None,
        metadata={"help": "Maximum size of each safetensors file"},
    )
    token: str = field(
        default=None,
        metadata={"help": "The modelers.cn token to download model from private repo."},
    )

    def __post_init__(self):
        if self.model_id:
            if self.model_name_or_path:
                raise ValueError(
                    "The parameters 'model_id' and 'model_name_or_path' cannot be passed simultaneously. Please choose one to provide."
                )
        else:
            if not self.model_name_or_path:
                raise ValueError("If model_id is not specified, model_name_or_path must be specified.")

        if self.split_special_tokens and self.use_fast_tokenizer:
            raise ValueError("`split_special_tokens` is only supported for slow tokenizers.")

        if self.new_special_tokens is not None:  # support multiple special tokens
            self.new_special_tokens = [token.strip() for token in self.new_special_tokens.split(",")]

        if self.load_in_4bit:
            if not _is_package_available("bitsandbytes"):
                raise RuntimeError("Please install bitsandbytes first before quantifying model.")

            if transformers.__version__ < "4.45.0":
                raise ValueError("The version of transformers is required at least 4.45.0 to run quantization.")
