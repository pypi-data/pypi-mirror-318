# Copyright (c) 2024 Huawei Technologies Co., Ltd.
# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This code is inspired by the pytorch's torchtune library.
# https://github.com/pytorch/torchtune
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
import sys

from openmind.utils.constants import DYNAMIC_ARG, SPECIFIED_ARGS
from openmind.utils import is_torch_available
from openmind.cli.list import List
from openmind.cli.lmeval import LMEVAL
from openmind.cli.pull import Pull
from openmind.cli.push import Push
from openmind.cli.rm import Rm
from openmind.cli.run import Run
from openmind.cli.env import Env
from openmind.cli.deploy.deploy import Deploy

# all supported CLI entrance names should be appended here
ENTRANCE_NAMES = ["list", "lmeval", "pull", "push", "rm", "chat", "run", "env", "deploy", "train", "export"]

# CLI entrance name that receiving dynamic argument should be appended here.
# For example:
# openmind-cli chat [dynamic] --xxx xxx, position [dynamic]  can be set as task name, model id or local model path.
DYNAMIC_ARGUMENT_ENTRANCE_NAMES = ["pull", "push", "rm", "chat", "run", "deploy", "train", "export"]


class OpenMindCLIParser:
    """Holds all information related to running the CLI"""

    def __init__(self):
        # Initialize the top-level parser
        self._parser = argparse.ArgumentParser(
            prog="openmind-cli",
            description="Welcome to the openMind CLI!",
            add_help=True,
        )
        # Default command is to print help
        self._parser.set_defaults(func=lambda args: self._parser.print_help())

        # Add subcommands
        subparsers = self._parser.add_subparsers(title="subcommands")
        List.create(subparsers)
        LMEVAL.create(subparsers)
        Pull.create(subparsers)
        Push.create(subparsers)
        Rm.create(subparsers)
        Run.create(subparsers)
        Env.create(subparsers)
        Deploy.create(subparsers)

        # Chat only support PyTorch Framework for now
        if is_torch_available():
            from openmind.cli.chat import Chat
            from openmind.cli.train import Train
            from openmind.cli.export import Export

            Chat.create(subparsers)
            Train.create(subparsers)
            Export.create(subparsers)

    def parse_args(self) -> dict:
        """Parse CLI arguments"""
        if len(sys.argv) == 1:
            raise ValueError(f"please specify CLI entrance name, currently support: {ENTRANCE_NAMES}")

        cli_entrance_name = sys.argv[1]

        if cli_entrance_name not in ENTRANCE_NAMES:
            raise ValueError(f"CLI entrance name `{cli_entrance_name}` is invalid, currently support: {ENTRANCE_NAMES}")

        known_args, unknown_args = self._parser.parse_known_args()
        known_args = vars(known_args)

        if cli_entrance_name in DYNAMIC_ARGUMENT_ENTRANCE_NAMES:
            unknown_args = _trans_args_list_to_dict(unknown_args, allow_dynamic_argument=True)
            specified_args = _trans_args_list_to_dict(sys.argv[3:])
        else:
            unknown_args = _trans_args_list_to_dict(unknown_args)
            specified_args = _trans_args_list_to_dict(sys.argv[2:])

        if SPECIFIED_ARGS in unknown_args:
            raise ValueError(f"name `{SPECIFIED_ARGS}` in not supported for manually specifying in CLI.")

        unknown_args[SPECIFIED_ARGS] = specified_args
        known_args.update(unknown_args)

        return known_args

    def run(self, args: argparse.Namespace) -> None:
        """Execute CLI"""
        args.func(args)


def main():
    parser = OpenMindCLIParser()
    args = parser.parse_args()
    parser.run(argparse.Namespace(**args))


def _trans_args_list_to_dict(args_list: list, allow_dynamic_argument: bool = False) -> dict:
    dynamic_arg_dict = {}

    if allow_dynamic_argument:
        if not args_list:
            raise ValueError(
                "a dynamic argument is required, such as task name/repo id. If train or export is used, please pass a yaml file."
            )

        dynamic_arg = args_list.pop(0)

        # dynamic argument should not be a key
        if dynamic_arg.startswith("--"):
            raise ValueError(f"dynamic argument should not start with `--`, but got {dynamic_arg}")

        if DYNAMIC_ARG in args_list:
            raise ValueError(f"name `{DYNAMIC_ARG}` in not supported for manually specifying in CLI.")

        dynamic_arg_dict[DYNAMIC_ARG] = dynamic_arg

    if len(args_list) % 2 != 0:
        raise ValueError(f"arguments in CLI should be specified in paris, but got {args_list}")

    args_dict = {}
    args_dict.update(dynamic_arg_dict)

    for idx in range(0, len(args_list), 2):
        key = args_list[idx]
        val = args_list[idx + 1]

        if not key.startswith("--"):
            raise ValueError(f"specified argument name `{key}` in CLI should start with `--`")

        if val.startswith("--"):
            raise ValueError(f"specified argument value `{val}` of key `{key}` in CLI should not start with `--`")

        args_dict[key.lstrip("-")] = val

    return args_dict


if __name__ == "__main__":
    main()
