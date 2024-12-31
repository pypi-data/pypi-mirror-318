# Copyright (c) OpenMMLab. All rights reserved.
from dataclasses import dataclass
from typing import Any, Dict, List, Literal

import torch


def _update_torch_dtype(config: 'ModelConfig', dtype: str):
    """Update the torch dtype from the model config.

    Args:
        config (ModelConfig): The input model config.
        dtype (str): user specified data type. Refer to
            `PyTorchEngineConfig.dtype` for detailed info
    """
    from lmdeploy.utils import get_logger
    logger = get_logger('lmdeploy')

    quantization_config = getattr(config.hf_config, 'quantization_config',
                                  dict())
    quant_method = quantization_config.get('quant_method', None)
    if quant_method == 'awq':
        logger.debug('set torch_dtype to float16 for awq.')
        config.hf_config.torch_dtype = 'float16'
        config.dtype = torch.float16
        return config

    torch_dtype = getattr(config.hf_config, 'torch_dtype', None)
    # deal with case when torch_dtype is not string but torch.dtype
    if isinstance(torch_dtype, torch.dtype):
        torch_dtype = str(torch_dtype).split('.')[1]

    if torch_dtype is None:
        _dtype = 'float16' if dtype == 'auto' else dtype
        logger.warning('Model config does not have `torch_dtype`,'
                       f' use: {_dtype}')
        torch_dtype = _dtype
        # update hf_config as well
        setattr(config.hf_config, 'torch_dtype', torch_dtype)
    else:
        # change to user specified data type if it is not 'auto'
        if dtype == 'auto':
            torch_dtype = torch_dtype if torch_dtype in [
                'float16', 'bfloat16'
            ] else 'float16'
        else:
            torch_dtype = dtype
    config.dtype = eval(f'torch.{torch_dtype}')
    return config


@dataclass
class BackendConfig:
    """backend config."""
    eager_mode: bool = True
    device_type: str = 'cuda'


@dataclass
class SchedulerConfig:
    """Config of scheduler."""

    max_batches: int
    max_session_len: int
    max_request_output_len: int = 512
    eviction_type: str = 'recompute'
    prefill_interval: int = 16
    max_active_adapters: int = 64


@dataclass
class CacheConfig:
    """Config of key value cache."""

    max_batches: int
    block_size: int
    num_cpu_blocks: int
    num_gpu_blocks: int
    window_size: int = -1
    cache_max_entry_count: float = 0.8
    max_prefill_token_num: int = 4096
    enable_prefix_caching: bool = False
    quant_policy: Literal[0, 4, 8] = 0
    device_type: str = 'cuda'

    def __post_init__(self):
        """post init."""
        from lmdeploy.utils import get_logger
        logger = get_logger('lmdeploy')
        if self.window_size > 1 and self.enable_prefix_caching:
            logger.warning(
                'Prefix caching is not available for window attention.')
            self.enable_prefix_caching = False


@dataclass
class ModelConfig:
    """Config of model."""

    hidden_size: int
    num_layers: int
    num_attention_heads: int
    num_key_value_heads: int
    bos_token_id: int
    eos_token_id: List[int]
    head_dim: int
    k_head_dim: int = None
    v_head_dim: int = None
    sliding_window: int = -1
    dtype: torch.dtype = torch.float16
    vocab_size: int = 40000
    hf_config: Any = None
    cogvlm_style: bool = False
    custom_module_map: Dict[str, setattr] = None

    def get_head_size(self):
        """get head size."""
        return self.head_dim

    @classmethod
    def from_pretrained(cls,
                        pretrained_model_name_or_path: str,
                        trust_remote_code: bool = True,
                        dtype: str = 'auto',
                        tp: int = 1):
        """Instantiate one of the configuration classes of the library from a
        pretrained model configuration.

        Args:
            pretrained_model_name_or_path (str): the pretrained model path
            trust_remote_code (bool):  Whether or not to allow for custom
                models defined on the Hub in their own modeling files.
            dtype (str): user specified data type for model weights and
                activations. Refer to `PyTorchEngineConfig` for details
        """
        from transformers import AutoConfig
        hf_config = AutoConfig.from_pretrained(
            pretrained_model_name_or_path, trust_remote_code=trust_remote_code)
        if getattr(hf_config, 'model_type', None) in ['phi3']:
            # phi3 + trust_remote_code leads to error when tp.
            hf_config = AutoConfig.from_pretrained(
                pretrained_model_name_or_path)
        return cls.from_hf_config(hf_config,
                                  pretrained_model_name_or_path,
                                  dtype=dtype,
                                  tp=tp)

    @classmethod
    def from_hf_config(cls,
                       hf_config: Any,
                       model_path: str = None,
                       dtype: str = 'auto',
                       tp: int = 1):
        """from huggingface config."""
        from lmdeploy.pytorch.configurations import AutoModelConfigBuilder

        model_config = AutoModelConfigBuilder.build(hf_config,
                                                    model_path,
                                                    tp=tp)

        if model_config.k_head_dim is None:
            assert model_config.head_dim is not None
            model_config.k_head_dim = model_config.head_dim
        if model_config.v_head_dim is None:
            assert model_config.head_dim is not None
            model_config.v_head_dim = model_config.head_dim

        # check for tp
        assert model_config.num_attention_heads % tp == 0
        if model_config.num_key_value_heads >= tp:
            assert model_config.num_key_value_heads % tp == 0
        else:
            assert tp % model_config.num_key_value_heads == 0

        # should after setting `hf_config` and `model_arch` attributes
        model_config = _update_torch_dtype(model_config, dtype)

        # update eos_token_id to list
        if isinstance(model_config.eos_token_id, int):
            model_config.eos_token_id = [model_config.eos_token_id]

        return model_config
