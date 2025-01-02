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
import socket
from transformers import Seq2SeqTrainingArguments


def get_swanlab_callbacks(training_args: Seq2SeqTrainingArguments):
    r"""
    Init SwanLabCallback to track experiments
    """
    if "swanlab" not in training_args.report_to:
        return None

    import swanlab
    from swanlab.integration.transformers import SwanLabCallback

    # The initialization of the trainer in transformers will verify the report_to hyperparameter.
    # The logging_dir hyperparameter in transformers does not support swanlab
    # so the swanlab in report_to is removed
    training_args.report_to.remove("swanlab")

    if int(os.environ.get("LOCAL_RANK", -1)) != 0:
        return None

    swanlab_default_dir = os.path.join(os.getcwd(), "swanlablog")
    swanlab.init(
        # The logging_dir hyperparameter in transformers is used for tensorboard.
        # Will default to 'output_dir/runs/**CURRENT_DATETIME_HOSTNAME**'
        logdir=(
            swanlab_default_dir if _is_tensorboard_default_dir(training_args.logging_dir) else training_args.logging_dir
        ),
        # Offline experiment tracking mode
        mode="local",
    )
    swanlab_callback = SwanLabCallback()
    return [swanlab_callback]


def _is_tensorboard_default_dir(logging_dir):
    basename = os.path.basename(logging_dir)
    hostname = socket.gethostname()
    return basename.endswith(hostname)
