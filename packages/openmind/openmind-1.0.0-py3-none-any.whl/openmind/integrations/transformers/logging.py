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

from openmind.utils.patch_utils import _apply_patches


def patch_transformers_logging():
    # patch logging
    from transformers.utils import logging as hf_logging

    from openmind.utils import logging

    patch_list = [
        ("get_logger", logging.get_logger),
        ("set_verbosity_info", logging.set_verbosity_info),
        ("set_verbosity_critical", logging.set_verbosity_critical),
        ("set_verbosity_error", logging.set_verbosity_error),
        ("set_verbosity_debug", logging.set_verbosity_debug),
        ("set_verbosity_warning", logging.set_verbosity_warning),
        ("set_verbosity", logging.set_verbosity),
    ]
    _apply_patches(patch_list, hf_logging)
