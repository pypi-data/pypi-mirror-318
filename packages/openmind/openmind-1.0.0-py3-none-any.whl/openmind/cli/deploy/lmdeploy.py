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
import subprocess
from ...utils import logging

logger = logging.get_logger()
logging.set_verbosity_info()


class DeployLMDeploy:
    def __init__(self, args: argparse.Namespace):
        logger.warning(
            "LMDeploy requires PyTorch version 2.3.1, which is different from the default version 2.1.0 used by openmind."
        )
        self.args = args
        self.port = args.port
        self.model_id = args.model_id
        self.host_model_path = args.host_model_path

    def deploy(self):
        command = [
            "lmdeploy",
            "serve",
            "api_server",
            "--server-name",
            "127.0.0.1",
            "--server-port",
            str(self.port),
            "--backend",
            "pytorch",
            "--model-name",
            self.model_id,
            "--device",
            "ascend",
            "--eager-mode",
            self.host_model_path,
        ]

        logger.info(f"Starting lmdeploy API server with command: {command}")
        try:
            subprocess.run(command)
        except Exception as err:
            logger.error(f"Error starting LMDeploy service: {err}")
