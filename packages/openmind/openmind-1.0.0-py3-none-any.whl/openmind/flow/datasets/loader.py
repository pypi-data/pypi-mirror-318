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
import json
from functools import partial

import numpy as np
from transformers import AutoTokenizer, Seq2SeqTrainingArguments
from openmind.utils import get_logger
from openmind.utils.constants import DATASET_INFO_CONFIG
from openmind.integrations.datasets import load_dataset
from ..datasets.preprocess import align_dataset, preprocess_supervised_dataset, merge_datasets
from .template import Template
from ..arguments import DatasetsArguments, FinetuneArguments
from .parser import get_dataset_list


logger = get_logger(__name__)


def _load_datasets(datasets_args: DatasetsArguments, training_args: Seq2SeqTrainingArguments):
    current_path = os.path.dirname(os.path.abspath(__file__))
    dataset_info_path = os.path.join(current_path, "../configs", DATASET_INFO_CONFIG)
    with open(dataset_info_path, "r") as f:
        dataset_info = json.load(f)

    if datasets_args.custom_dataset_info is not None:
        custom_dataset_path_list = [
            custom_dataset_path.strip(" ") for custom_dataset_path in datasets_args.custom_dataset_info.split(",")
        ]
        for custom_dataset_path in custom_dataset_path_list:
            with open(custom_dataset_path, "r") as f:
                custom_dataset_info = json.load(f)
                dataset_info.update(custom_dataset_info)

    dataset_list = [dataset.strip(" ") for dataset in datasets_args.dataset.split(",")]
    aligned_datasets = []
    for name in dataset_list:
        dataset_attr = get_dataset_list(name, dataset_info)
        dataset = load_dataset(
            path=dataset_attr.load_from,
            data_files=dataset_attr.file_name,
            name=datasets_args.subset_name,
            split=dataset_attr.split,
        )

        # The columns of the original dataset can be deleted because only the tokenized data is saved.
        column_names = dataset.column_names
        logger.debug("Column_names to be deleted = {}".format(column_names))

        if dataset_attr.num_samples is not None:
            target_num = min(dataset_attr.num_samples, len(dataset))
            indexes = np.random.permutation(len(dataset))[:target_num]

            dataset = dataset.select(indexes)
            logger.info("Sampled {} examples from dataset {}.".format(target_num, dataset_attr))

        aligned_datasets.append(align_dataset(dataset_attr, dataset, datasets_args, training_args))
    return aligned_datasets


def get_dataset(
    datasets_args: DatasetsArguments,
    training_args: Seq2SeqTrainingArguments,
    finetune_args: FinetuneArguments,
    tokenizer: AutoTokenizer,
    template: Template,
):
    with training_args.main_process_first(desc="load dataset"):
        aligned_datasets = _load_datasets(datasets_args, training_args)
        merged_dataset = merge_datasets(aligned_datasets)
        logger.debug("Finish load data, Sft_datasets = {}".format(merged_dataset))

    with training_args.main_process_first(desc="preprocess dataset"):
        column_names = merged_dataset.column_names
        preprocess_kwargs = dict(
            num_proc=datasets_args.preprocessing_num_workers,
            load_from_cache_file=training_args.local_process_index != 0,
            desc="Start running tokenizer on datasets",
        )
        # TODO (#12) Currently, the following prompts exist:
        # The current process just got forked, after parallelism has already been used.
        # Disabling parallelism to avoid deadlocks
        if finetune_args.stage == "sft":
            preprocess_func = partial(
                preprocess_supervised_dataset, template=template, tokenizer=tokenizer, datasets_args=datasets_args
            )
        else:
            # TODO (#13) Support multiple processing methods such as pt and rm.
            raise NotImplementedError

        merged_dataset = merged_dataset.map(
            preprocess_func,
            batched=True,
            batch_size=datasets_args.preprocessing_batch_size,
            remove_columns=column_names,
            **preprocess_kwargs,
        )
    return merged_dataset
