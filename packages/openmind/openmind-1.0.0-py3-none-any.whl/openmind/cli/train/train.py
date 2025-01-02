# Copyright (c) 2024 Huawei Technologies Co., Ltd.
# Copyright 2024 the LlamaFactory team.
# This code is inspired by the LlamaFactory's cli feature.
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
import subprocess
import random
import sys
import argparse
import textwrap
import torch
from accelerate import Accelerator

from openmind.cli.subcommand import SubCommand
from . import run_train


class Train(SubCommand):

    def __init__(self, subparsers: argparse._SubParsersAction):
        super().__init__()
        self._parser = subparsers.add_parser(
            "train",
            prog="openmind-cli trian",
            help="loading yaml file to start finetune",
            description="loading yaml file to start finetune",
            epilog=textwrap.dedent(
                """\
            examples:
                $ openmind-cli train xxx.yaml
                ...
            """
            ),
            formatter_class=argparse.RawTextHelpFormatter,
        )
        self._add_arguments()
        self._parser.set_defaults(func=self._train_cmd)

    def get_device_count(self):
        accelerator = Accelerator()
        device_module = getattr(torch, accelerator.device.type, None)
        if device_module and hasattr(device_module, "device_count"):
            return device_module.device_count()
        return 0

    def _train_cmd(self, args: argparse.Namespace):
        if self.get_device_count() > 1:
            master_addr = os.environ.get("MASTER_ADDR", "127.0.0.1")
            master_port = os.environ.get("MASTER_PORT", str(random.randint(20001, 29999)))
            command = [
                "torchrun",
                "--nnodes",
                os.environ.get("NNODES", "1"),
                "--node_rank",
                os.environ.get("RANK", "0"),
                "--nproc_per_node",
                os.environ.get("NPROC_PER_NODE", str(self.get_device_count())),
                "--master_addr",
                master_addr,
                "--master_port",
                master_port,
                run_train.__file__,
                "--yaml_file",
                sys.argv[-1],
            ]
            subprocess.run(command)
        elif self.get_device_count() == 1:
            python_executable = sys.executable
            command = [
                python_executable,
                run_train.__file__,
                "--yaml_file",
                sys.argv[-1],
            ]
            subprocess.run(command)
        else:
            raise ValueError("There is no npu devices to launch finetune workflow")
