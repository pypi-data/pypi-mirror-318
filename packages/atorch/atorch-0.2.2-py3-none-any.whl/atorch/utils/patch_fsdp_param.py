from typing import Callable, Optional

import torch
from torch import nn

from atorch.common.constants import FSDPConstants
from atorch.common.singleton import SingletonMeta
from atorch.utils.version import torch_version

if torch_version() >= (2, 4, 0):  # type: ignore
    from torch.distributed._composable.fsdp import _fsdp_init
    from torch.distributed._composable.fsdp._fsdp_param import FSDPParam
    from torch.distributed._composable.fsdp._fsdp_state import FSDPState
    from torch.distributed._tensor.api import DTensor
else:
    FSDPParam = object


class FSDP2PatchContext(metaclass=SingletonMeta):
    ORIGINAL_FSDP_STATE_PRE_BACKWARD: Optional[Callable] = None
    ORIGINAL_GET_MANAGED_STATES: Optional[Callable] = None
    ORIGINAL_INIT_SHARDED_PARAM: Optional[Callable] = None


def patch_fsdp2_init_sharded_param():
    assert torch_version() >= (2, 4, 0)  # type: ignore

    if FSDP2PatchContext().ORIGINAL_INIT_SHARDED_PARAM is not None:
        return

    @torch.no_grad()
    def _atorch_init_sharded_param_wrapper(self, param: nn.Parameter, device: torch.device):
        FSDP2PatchContext().ORIGINAL_INIT_SHARDED_PARAM(self, param, device)

        if hasattr(param, FSDPConstants.CHECKPOINT_NAME):
            setattr(self.sharded_param, FSDPConstants.CHECKPOINT_NAME, param.checkpoint_name)
        if not hasattr(self.sharded_param, FSDPConstants.ATORCH_FSDP2_SHARDED):
            setattr(self.sharded_param, FSDPConstants.ATORCH_FSDP2_SHARDED, True)

    FSDP2PatchContext().ORIGINAL_INIT_SHARDED_PARAM = FSDPParam._init_sharded_param
    FSDPParam._init_sharded_param = _atorch_init_sharded_param_wrapper


def patch_fsdp2_get_managed_states():
    assert torch_version() >= (2, 4, 0)  # type: ignore

    if FSDP2PatchContext().ORIGINAL_GET_MANAGED_STATES is not None:
        return

    def _atorch_get_managed_states_wrapper(modules):
        params, buffers = FSDP2PatchContext().ORIGINAL_GET_MANAGED_STATES(modules)
        selected_params = []
        for param in params:
            if not (isinstance(param, DTensor) and getattr(param, FSDPConstants.ATORCH_FSDP2_SHARDED, False)):
                selected_params.append(param)

        return selected_params, buffers

    FSDP2PatchContext().ORIGINAL_GET_MANAGED_STATES = _fsdp_init._get_managed_states
    _fsdp_init._get_managed_states = _atorch_get_managed_states_wrapper


def patch_fsdp2_pre_backward():
    assert torch_version() >= (2, 4, 0)  # type: ignore

    if FSDP2PatchContext().ORIGINAL_FSDP_STATE_PRE_BACKWARD is not None:
        return

    def _atorch_pre_backward_wrapper(self, grad: torch.Tensor) -> torch.Tensor:
        grad = FSDP2PatchContext().ORIGINAL_FSDP_STATE_PRE_BACKWARD(self, grad)

        if hasattr(self, "_inter_state"):
            inter_ggm_state = getattr(self, "_inter_state")
            inter_ggm_state._pre_backward(None)
        return grad

    FSDP2PatchContext().ORIGINAL_FSDP_STATE_PRE_BACKWARD = FSDPState._pre_backward
    FSDPState._pre_backward = _atorch_pre_backward_wrapper
