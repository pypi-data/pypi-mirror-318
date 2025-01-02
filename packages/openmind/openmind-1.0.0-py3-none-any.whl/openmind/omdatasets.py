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

import warnings
from typing import Optional, Sequence, Mapping, Union

from openmind.integrations.datasets import DownloadMode, load_dataset


warnings.warn(
    "The class 'OmDataset' is deprecated and will be removed in a future release. "
    "Please use the 'load_dataset' function from 'openmind.integrations.datasets' instead: "
    "'from openmind.integrations.datasets import load_dataset'.",
    FutureWarning,
)


class OmDataset:
    @staticmethod
    def load_dataset(
        path: Optional[str] = None,
        name: Optional[str] = None,
        revision: Optional[str] = "main",
        split: Optional[str] = None,
        data_dir: Optional[str] = None,
        data_files: Optional[Union[str, Sequence[str], Mapping[str, Union[str, Sequence[str]]]]] = None,
        download_mode: Optional[DownloadMode] = DownloadMode.REUSE_DATASET_IF_EXISTS,
        cache_dir: Optional[str] = None,
        token: Optional[str] = None,
        dataset_info_only: Optional[bool] = False,
        trust_remote_code: bool = None,
        streaming: bool = False,
        **config_kwargs,
    ):
        return load_dataset(
            path,
            name,
            revision,
            split,
            data_dir,
            data_files,
            download_mode,
            cache_dir,
            token,
            dataset_info_only,
            trust_remote_code,
            streaming,
            **config_kwargs,
        )
