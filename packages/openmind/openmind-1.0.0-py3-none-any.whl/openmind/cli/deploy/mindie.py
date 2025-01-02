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

import docker
from docker.errors import ContainerError, APIError

from ...utils import logging

SPECIAL_PORTS_LIMIT = 1024

logger = logging.get_logger()
logging.set_verbosity_info()

MINDIE_IMAGE_NAME = "registry.modelers.cn/base_image/mindie:1.0.RC3-800I-A2-arm64-OpenMind"
PATH_IN_CONTAINER = "/home/HwHiAiUser/Ascend"

CONTAINER_NAME = "mindie-service"


class DeployMindie:
    def __init__(self, args):
        self.args = args
        self.port = args.port
        self.model_id = args.model_id
        self.host_model_path = args.host_model_path

    @property
    def npu_device_ids(self):
        npu_device_ids = "0,1,2,3"
        if isinstance(self.args.npu_device_ids, str):
            if not all(0 <= int(num) <= 7 for num in self.args.npu_device_ids.split(",")):
                raise ValueError("Device id must be in range 0 ~ 7 .")
            npu_device_ids = self.args.npu_device_ids
        elif self.args.npu_device_ids is None:
            logger.info("Use default npu_device_ids '0,1,2,3'")
        else:
            raise TypeError("npu_device_ids data type error, please check data type!")
        return npu_device_ids

    @staticmethod
    def stop_service(remind=False):
        client = docker.from_env()
        containers = client.containers.list(all=True)
        if any(CONTAINER_NAME == container.name for container in containers):
            container = client.containers.get(CONTAINER_NAME)
            container.remove(force=True)
            if remind:
                logger.info("Stop mindie service success.")
        elif remind:
            logger.info("There is no mindie daemon service to stop.")

    def deploy(self):
        self._init_param()
        self._start_container()

    def generate_npu_device_id(self):
        return ",".join(str(num) for num in range(self.args.world_size))

    def _init_param(self):
        if len(self.npu_device_ids.split(",")) != self.args.world_size:
            raise ValueError("Length of npu_device_ids should be equal with world_size.")

    def _start_container(self):
        self.stop_service()

        client = docker.from_env()
        model_path = os.path.join(PATH_IN_CONTAINER, self.host_model_path.rstrip("/").split("/")[-1])
        devices = [f"/dev/davinci{i}" for i in self.npu_device_ids.split(",")]
        devices.extend(["/dev/davinci_manager", "/dev/hisi_hdc", "/dev/devmm_svm"])
        volumes = [
            "/usr/local/Ascend/driver:/usr/local/Ascend/driver",
            "/usr/local/sbin:/usr/local/sbin",
            "/usr/local/dcmi:/usr/local/dcmi",
            "/usr/local/bin/npu-smi:/usr/local/bin/npu-smi",
            f"{self.host_model_path}:{model_path}",
        ]

        device_in_container = self.generate_npu_device_id()

        command = (
            f"--model {model_path} "
            f"--port {self.port} "
            f"--npu-device-ids '{device_in_container}' "
            f"--world-size {self.args.world_size} "
        )

        try:
            container = client.containers.run(
                image=MINDIE_IMAGE_NAME,
                command=command,
                name=CONTAINER_NAME,
                volumes=volumes,
                ports={f"{self.port}": f"{self.port}"},
                devices=devices,
                detach=True,
            )
            logs = container.logs(stream=True, follow=True)
            for log in logs:
                output = log.decode("utf-8")
                if "Daemon start success" in output:
                    logger.info("Docker run and container init success! ")
                    break
                elif "Fail to get model config path" in output:
                    logger.error("Failed to run MindIE. Please check your model weight path.")
                    break
                elif "Failed to run mindieservice_daemon" in output or "Failed to init endpoint" in output:
                    logger.error("Failed to run MindIE. Please check docker logs.")
                    break

        except (ContainerError, APIError) as err:
            logger.error(f"There is an error during container initialization:{err}")
