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

import argparse

from openmind.flow.arguments import get_all_args
from openmind.flow.trainer.sft_trainer import run_sft
from openmind.flow.callbacks import get_swanlab_callbacks


def run_train(yaml_file):
    dataset_args, model_args, training_args, finetune_args = get_all_args(yaml_file)
    callbacks = get_swanlab_callbacks(training_args)
    if finetune_args.stage == "sft":
        run_sft(dataset_args, model_args, training_args, finetune_args, callbacks)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--yaml_file", "--optional", type=str)

    args = parser.parse_args()
    run_train(args.yaml_file)
