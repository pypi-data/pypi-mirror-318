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

import os
from typing import TYPE_CHECKING

from .version import __version__

# To temporarily avoid import errors. When openmind is imported firstly, the code will throw an error,
# so it is necessary to import mindspore first.
from .utils import is_torch_available, is_transformers_available


# Direct imports for type-checking
if TYPE_CHECKING:
    from .utils import (
        get_framework,
        is_ms_available,
        is_torch_available,
        is_torch_npu_available,
        is_mindformers_available,
        is_transformers_available,
        is_diffusers_available,
        is_mindone_available,
        is_mindnlp_available,
        is_tokenizers_available,
        is_lmeval_available,
        is_lmdeploy_available,
        logging,
    )
    from .archived.models.auto import (
        AutoConfig,
        AutoFeatureExtractor,
        AutoImageProcessor,
        AutoModel,
        AutoModelForCausalLM,
        AutoModelForSequenceClassification,
        AutoProcessor,
        AutoTokenizer,
    )
    from .archived.trainers import (
        Trainer,
        TrainingArguments,
        PreTrainer,
        PreTrainingArguments,
    )
    from .archived.pipelines import pipeline
    from .omdatasets import OmDataset
else:
    from sys import modules as sys_modules
    from .utils import _LazyModule

    _import_structure = {
        "utils": [
            "get_framework",
            "is_ms_available",
            "is_torch_available",
            "is_torch_npu_available",
            "is_mindformers_available",
            "is_transformers_available",
            "is_diffusers_available",
            "is_mindone_available",
            "is_mindnlp_available",
            "is_tokenizers_available",
            "is_lmeval_available",
            "is_lmdeploy_available",
            "logging",
        ],
        "archived": [],
        "archived.models": [],
        "archived.models.auto": [
            "AutoConfig",
            "AutoFeatureExtractor",
            "AutoImageProcessor",
            "AutoModel",
            "AutoModelForCausalLM",
            "AutoModelForSequenceClassification",
            "AutoProcessor",
            "AutoTokenizer",
        ],
        "archived.pipelines": ["pipeline"],
        "archived.trainers": ["Trainer", "TrainingArguments", "PreTrainer", "PreTrainingArguments"],
        "omdatasets": ["OmDataset"],
    }

    sys_modules[__name__] = _LazyModule(
        __name__,
        globals()["__file__"],
        _import_structure,
        module_spec=__spec__,
        extra_objects={"__version__": __version__},
    )

# apply patch at once when openmind is imported
if is_torch_available() and is_transformers_available():
    import openmind.integrations.transformers

OPENMIND_HIDE_STACKTRACE = os.getenv("OPENMIND_HIDE_STACKTRACE", "TRUE")

if OPENMIND_HIDE_STACKTRACE not in ["TRUE", "true", "FALSE", "false"]:
    raise ValueError(
        "Environment variable `OPENMIND_HIDE_STACKTRACE` is invalid, "
        "supported values: ['TRUE', 'true', 'FALSE', 'false']"
    )

if OPENMIND_HIDE_STACKTRACE in ["TRUE", "true"]:
    import sys

    sys.tracebacklimit = 0
