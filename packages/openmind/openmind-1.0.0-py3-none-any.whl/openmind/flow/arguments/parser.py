# Copyright (c) 2024 Huawei Technologies Co., Ltd.
# Copyright 2024 the LlamaFactory team.
#
# Adapt some arguments parser method from llamafactory
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

import os

from transformers import HfArgumentParser, Seq2SeqTrainingArguments
from transformers.trainer_utils import get_last_checkpoint

from openmind.utils import logging
from openmind.utils.import_utils import is_swanlab_available
from .data_args import DatasetsArguments
from .model_args import ModelArguments
from .finetune_args import FinetuneArguments


_ALL_ARGS = [DatasetsArguments, ModelArguments, Seq2SeqTrainingArguments, FinetuneArguments]
_EXPORT_ARGS = [ModelArguments, Seq2SeqTrainingArguments]

logger = logging.get_logger(__name__)


def _parse_args(parser: "HfArgumentParser", path=None):

    return parser.parse_yaml_file(path)


def get_all_args(path):
    parser = HfArgumentParser(_ALL_ARGS)
    dataset_args, model_args, training_args, finetune_args = _parse_args(parser, path)

    # Detecting last checkpoint
    if os.path.isdir(training_args.output_dir) and training_args.do_train and not training_args.overwrite_output_dir:
        last_checkpoint = get_last_checkpoint(training_args.output_dir)
        if last_checkpoint is None and len(os.listdir(training_args.output_dir)) > 0:
            raise ValueError(
                f"Output directory ({training_args.output_dir}) already exists and is not empty. "
                "Set overwrite_output_dir true to overcome."
            )
        elif last_checkpoint is not None and training_args.resume_from_checkpoint is None:
            training_args.resume_from_checkpoint = last_checkpoint
            logger.info_rank0(
                f"Checkpoint detected, resuming training at {last_checkpoint}. To avoid this behavior, change "
                "the `output_dir` or set `overwrite_output_dir` true to train from scratch."
            )

    if model_args.use_gradient_checkpointing:
        # When gradient checkpointing was enabled, ddp_find_unused_parameters need to be False.
        # According to: https://github.com/huggingface/peft/issues/313#issuecomment-1517391550
        training_args.ddp_find_unused_parameters = False

    if "swanlab" in training_args.report_to:
        if not is_swanlab_available():
            raise ModuleNotFoundError("swanlab module is not installed.Please install it using 'pip install swanlab'.")
    elif bool(training_args.report_to):
        logger.warning(
            "It is recommended to use swanlab to track experiment, "
            "and other tools have not been fully validated in openMind."
        )

    return dataset_args, model_args, training_args, finetune_args


def get_export_args(path):
    parser = HfArgumentParser(_EXPORT_ARGS)
    model_args, training_args = _parse_args(parser, path)

    return model_args, training_args
