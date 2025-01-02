# Copyright (c) 2024 Huawei Technologies Co., Ltd.
# Copyright 2024 The HuggingFace Inc. team. All rights reserved.
#
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

import torch
import transformers
from transformers.utils import is_torch_npu_available, is_torch_xpu_available
from transformers.modeling_utils import PreTrainedModel
from transformers.quantizers.quantizers_utils import get_module_from_name
from transformers.pytorch_utils import Conv1D
from typing import Dict, Any, Optional, List


def create_quantized_param_patch(
    self,
    model: "PreTrainedModel",
    param_value: "torch.Tensor",
    param_name: str,
    target_device: "torch.device",
    state_dict: Dict[str, Any],
    unexpected_keys: Optional[List[str]] = None,
):
    """
    combines logic from _load_state_dict_into_meta_model and .integrations.bitsandbytes.py::set_module_quantized_tensor_to_device()
    """
    import bitsandbytes as bnb

    module, tensor_name = get_module_from_name(model, param_name)

    if tensor_name not in module._parameters:
        raise ValueError(f"{module} does not have a parameter or a buffer named {tensor_name}.")

    old_value = getattr(module, tensor_name)

    if isinstance(target_device, int) and is_torch_npu_available():
        target_device = f"npu:{target_device}"

    if tensor_name == "bias":
        if param_value is None:
            new_value = old_value.to(target_device)
        else:
            new_value = param_value.to(target_device)

        new_value = torch.nn.Parameter(new_value, requires_grad=old_value.requires_grad)
        module._parameters[tensor_name] = new_value
        return

    if not isinstance(module._parameters[tensor_name], bnb.nn.Params4bit):
        raise ValueError("this function only loads `Linear4bit components`")
    if (
        old_value.device == torch.device("meta")
        and target_device not in ["meta", torch.device("meta")]
        and param_value is None
    ):
        raise ValueError(f"{tensor_name} is on the meta device, we need a `value` to put in on {target_device}.")

    # construct `new_value` for the module._parameters[tensor_name]:
    if self.pre_quantized:
        # 4bit loading. Collecting components for restoring quantized weight
        # This can be expanded to make a universal call for any quantized weight loading

        if not self.is_serializable:
            raise ValueError(
                "Detected int4 weights but the version of bitsandbytes is not compatible with int4 serialization. "
                "Make sure to download the latest `bitsandbytes` version. `pip install --upgrade bitsandbytes`."
            )

        if (param_name + ".quant_state.bitsandbytes__fp4" not in state_dict) and (
            param_name + ".quant_state.bitsandbytes__nf4" not in state_dict
        ):
            raise ValueError(
                f"Supplied state dict for {param_name} does not contain `bitsandbytes__*` and possibly other `quantized_stats` components."
            )

        quantized_stats = {}
        for k, v in state_dict.items():
            if param_name + "." in k:
                quantized_stats[k] = v
                if unexpected_keys is not None and k in unexpected_keys:
                    unexpected_keys.remove(k)

        param_kwargs = {}
        if self.is_bnb_supports_quant_storage_module:
            param_kwargs["module"] = module

        new_value = bnb.nn.Params4bit.from_prequantized(
            data=param_value,
            quantized_stats=quantized_stats,
            requires_grad=False,
            device=target_device,
            **param_kwargs,
        )
    else:
        new_value = param_value.to("cpu")

        # Support models using `Conv1D` in place of `nn.Linear` (e.g. openai-community/gpt2) by transposing the weight matrix prior to quantization.
        # Since weights are saved in the correct "orientation", we skip transposing when loading.
        if issubclass(module.source_cls, Conv1D):
            new_value = new_value.T

        kwargs = old_value.__dict__
        new_value = bnb.nn.Params4bit(new_value, requires_grad=False, **kwargs).to(target_device)

    module._parameters[tensor_name] = new_value


# Copied from transformers.quantizers.quantizer_bnb_8bit.Bnb8BitHfQuantizer.update_device_map
def update_device_map_patch(self, device_map):
    if device_map is None:
        if torch.cuda.is_available():
            device_map = {"": torch.cuda.current_device()}
        elif is_torch_npu_available():
            device_map = {"": f"npu:{torch.npu.current_device()}"}
        elif is_torch_xpu_available():
            device_map = {"": f"xpu:{torch.xpu.current_device()}"}
        else:
            device_map = {"": "cpu"}
    return device_map


def patch_bnb():
    transformers.quantizers.quantizer_bnb_4bit.Bnb4BitHfQuantizer.create_quantized_param = create_quantized_param_patch
    transformers.quantizers.quantizer_bnb_4bit.Bnb4BitHfQuantizer.update_device_map = update_device_map_patch
