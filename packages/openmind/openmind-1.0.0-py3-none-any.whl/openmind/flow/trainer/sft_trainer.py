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


from transformers import DataCollatorForSeq2Seq, Seq2SeqTrainingArguments, Seq2SeqTrainer, TrainerCallback
from typing import List, Optional

from openmind.utils import get_logger
from openmind.utils.constants import IGNORE_INDEX
from ..datasets import get_dataset
from ..datasets.template import TEMPLATES
from ..model import get_model, get_tokenizer
from ..model.model_registry import get_template_type
from ..arguments import DatasetsArguments, ModelArguments, FinetuneArguments


logger = get_logger(__name__)


def run_sft(
    dataset_args: DatasetsArguments,
    model_args: ModelArguments,
    training_args: Seq2SeqTrainingArguments,
    finetune_args: FinetuneArguments,
    callbacks: Optional[List["TrainerCallback"]] = None,
):
    tokenizer = get_tokenizer(model_args)
    model = get_model(model_args, finetune_args, training_args)
    template_type = get_template_type(model_args)
    template = TEMPLATES[template_type]
    dataset = get_dataset(dataset_args, training_args, finetune_args, tokenizer, template)

    data_collator = DataCollatorForSeq2Seq(
        tokenizer=tokenizer,
        padding="max_length" if dataset_args.max_length else True,
        pad_to_multiple_of=8 if training_args.do_train else None,
        max_length=dataset_args.max_length,
        label_pad_token_id=IGNORE_INDEX if dataset_args.ignore_pad_token_for_loss else tokenizer.pad_token_id,
    )

    trainer = Seq2SeqTrainer(
        model=model,
        args=training_args,
        tokenizer=tokenizer,
        data_collator=data_collator,
        train_dataset=dataset,
        eval_dataset=None,
        callbacks=callbacks,
    )

    if training_args.do_train:
        logger.info_rank0("Start training.")
        train_result = trainer.train(resume_from_checkpoint=training_args.resume_from_checkpoint)
        trainer.save_model()
        trainer.log_metrics("train", train_result.metrics)
        trainer.save_metrics("train", train_result.metrics)
        trainer.save_state()
