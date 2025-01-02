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
import importlib

from openmind.utils import is_transformers_available, is_torch_available, is_torch_npu_available

if is_transformers_available() and is_torch_available():
    import transformers
    from .autoclasses import *  # noqa: F403

    from .npu_fused_ops.modeling_utils import (
        patch_built_in_model,
        patch_remote_model,
        _npu_fused_ops_imp,
    )
    from .logging import patch_transformers_logging
    from .bitsandbytes import patch_bnb

    patch_transformers_logging()

    transformers.modeling_utils.PreTrainedModel._autoset_attn_implementation = _npu_fused_ops_imp
    patch_built_in_model()
    patch_remote_model()

    if importlib.util.find_spec("bitsandbytes") and is_torch_npu_available():
        patch_bnb()
