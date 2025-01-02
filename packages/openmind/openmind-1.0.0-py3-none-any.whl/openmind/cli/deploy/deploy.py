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
import textwrap
from ..subcommand import SubCommand
from .mindie import DeployMindie
from .lmdeploy import DeployLMDeploy
from ...utils.constants import DYNAMIC_ARG
from openmind.archived.pipelines.pipeline_utils import download_from_repo


class Deploy(SubCommand):
    """Holds all the logic for the 'openmind-cli deploy' subcommand."""

    def __init__(self, subparsers: argparse._SubParsersAction):
        super().__init__()
        self.host_model_path = None
        self._parser = subparsers.add_parser(
            "deploy",
            prog="openmind-cli deploy",
            help="Using mindie-service to Perform Inference via curl",
            description="Using mindie-service to Perform Inference via curl",
            epilog=textwrap.dedent(
                """\
            examples:
                $ openmind-cli deploy PyTorch-NPU/chatglm3_6b

                $ openmind-cli deploy PyTorch-NPU/chatglm3_6b --npu_device_ids [[0,1,2,3]]
                ...
            """
            ),
            formatter_class=argparse.RawDescriptionHelpFormatter,
        )
        self._add_arguments()
        self._parser.set_defaults(func=self._deploy_cmd)

    def _add_arguments(self) -> None:
        """Add arguments to the parser."""
        self._parser.add_argument(
            "--backend",
            type=str,
            default="mindie",
            help="inference backend, choosing from mindie and lmdeploy",
        )
        self._parser.add_argument(
            "--port",
            type=int,
            default=1025,
            help="port for the service-oriented deployment",
        )
        self._parser.add_argument(
            "--npu_device_ids",
            default="0,1,2,3",
            type=str,
            help="npu ids allocated to the model instance",
        )
        self._parser.add_argument(
            "--world_size",
            default=4,
            type=int,
            help="npu world size",
        )

    def _deploy_cmd(self, args: argparse.Namespace) -> None:
        """Using mindieservice to perform inference via curl"""
        args_dict = vars(args)
        args_dict.pop("func")
        args.model_id = args_dict.pop(DYNAMIC_ARG)
        if args.model_id == "stop":
            DeployMindie.stop_service(remind=True)
            return
        args.host_model_path = download_from_repo(args.model_id)

        if args.backend == "mindie":
            DeployMindie(args).deploy()
        elif args.backend == "lmdeploy":
            DeployLMDeploy(args).deploy()
        else:
            raise ValueError("backend only supports mindie and lmdeploy.")
