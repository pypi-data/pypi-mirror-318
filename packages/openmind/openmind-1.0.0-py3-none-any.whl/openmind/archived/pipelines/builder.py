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

import importlib
from typing import Any, Dict, Optional

from openmind.utils.logging import get_logger, set_verbosity_info
from .pipeline_utils import SUPPORTED_TASK_MAPPING, get_task_from_readme

logger = get_logger()
set_verbosity_info()


def _load_pipeline_class(pipeline_class_config):
    try:
        module_name, class_name = pipeline_class_config.rsplit(".", 1)
        module = importlib.import_module(f"openmind.archived.pipelines.{module_name}")
        pipeline_class = getattr(module, class_name)
        return pipeline_class
    except (AttributeError, ImportError) as e:
        raise ImportError(f"Failed to load pipeline class {pipeline_class_config}") from e


def _parse_native_json(task, framework, backend):
    config = SUPPORTED_TASK_MAPPING

    task_config = config.get(task)
    if task_config is None:
        raise KeyError(f"Task {task} has no config")
    if framework is None:
        framework = task_config.get("default_framework")
    framework_config = task_config.get(framework, {})

    if backend is None:
        backend = framework_config.get("default_backend")
    pipeline_config = framework_config.get(backend)

    return pipeline_config, framework, backend


def _validate_model_and_component(model, component, component_name):
    if model is None and component is not None:
        raise RuntimeError(
            f"Impossible to instantiate a pipeline with {component_name} specified but not the model as the provided"
            f" {component_name} may not be compatible with the default model. Please provide a PreTrainedModel class"
            f" or a path/identifier to a pretrained model when providing {component_name}."
        )


def build_pipeline(
    task: Optional[str] = None,
    model=None,
    config=None,
    tokenizer=None,
    feature_extractor=None,
    image_processor=None,
    framework: Optional[str] = None,
    backend: Optional[str] = None,
    model_kwargs: Dict[str, Any] = None,
    **kwargs,
):
    if task is None and model is None:
        raise RuntimeError(
            "Impossible to instantiate a pipeline without specifying either a task or a model. "
            "Please provide a task class or a model"
        )

    _validate_model_and_component(model, tokenizer, "tokenizer")
    _validate_model_and_component(model, feature_extractor, "feature_extractor")
    _validate_model_and_component(model, image_processor, "image_processor")

    if task is None and model is not None:
        if isinstance(model, str):
            task = get_task_from_readme(model)
        else:
            raise RuntimeError("task must be provided when the type of model is a model instance")

    # MindFormers only receive param `device_id` with integer type.
    if "device_id" in kwargs and not isinstance(kwargs["device_id"], int):
        try:
            kwargs["device_id"] = int(kwargs["device_id"])
        except ValueError as e:
            raise ValueError("The `device_id` parameter can not be converted to integer type.") from e

    pipeline_config, framework, backend = _parse_native_json(task, framework, backend)
    if not pipeline_config:
        raise ValueError(
            f"No pipeline config found for task '{task}' with the given framework '{framework}' and "
            f"backend '{backend}'"
        )
    supported_models = pipeline_config.get("supported_models")
    pipeline_class_config = pipeline_config.get("pipeline_class")

    if not pipeline_class_config or not supported_models:
        raise ValueError(
            f"Pipeline class or supported models are missing in the configuration for task '{task}', "
            f"framework '{framework}', and backend '{backend}'"
        )

    if model is None:
        if "@" in supported_models[0]:
            model, revision = supported_models[0].split("@")
            kwargs["revision"] = revision
        else:
            model = supported_models[0]

    pipeline_cls = _load_pipeline_class(pipeline_class_config)

    pipeline = pipeline_cls(
        task=task,
        model=model,
        config=config,
        tokenizer=tokenizer,
        feature_extractor=feature_extractor,
        image_processor=image_processor,
        framework=framework,
        backend=backend,
        model_kwargs=model_kwargs,
        **kwargs,
    )

    return pipeline
