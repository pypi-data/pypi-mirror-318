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

from openmind.utils.constants import Stages, FinetuneType


@dataclass
class LoraArguments:
    lora_target_modules: Optional[str] = field(
        default=None,
        metadata={
            "help": """
                   The target modules for LoRA fine-tuning. If you use model_id, it will use default lora_target_modules,
                   if you set to 'all', it will use all posiible target modules in model.
                   if you set specfic values, such as 'q_proj, v_proj', it will be applied to models.
                   """
        },
    )
    lora_alpha: Optional[int] = field(
        default=None,
        metadata={"help": "The scale factor for LoRA fine-tuning (default: lora_rank * 2)."},
    )
    lora_dropout: float = field(
        default=0.0,
        metadata={"help": "Dropout rate for the LoRA fine-tuning."},
    )
    lora_rank: int = field(
        default=8,
        metadata={"help": "The intrinsic dimension for LoRA fine-tuning."},
    )


@dataclass
class FinetuneArguments(LoraArguments):
    stage: str = field(
        default=Stages.SFT,
        metadata={"help": "Which stage will be used in training, currently only 'pt' and 'sft' are supported"},
    )
    finetuning_type: str = field(
        default=FinetuneType.FULL,
        metadata={"help": "Which fine-tuning method to use."},
    )

    def __post_init__(self):
        def split_arg(arg):
            if isinstance(arg, str):
                return [item.strip() for item in arg.split(",")]
            return arg

        if self.stage not in [Stages.SFT]:
            raise ValueError(f"Currently supported stage list  is [{Stages.SFT}]")

        if self.finetuning_type not in [FinetuneType.FULL, FinetuneType.LORA]:
            raise ValueError(
                f"Currently supported fine-tuning method list is [{FinetuneType.FULL}, {FinetuneType.LORA}]"
            )
