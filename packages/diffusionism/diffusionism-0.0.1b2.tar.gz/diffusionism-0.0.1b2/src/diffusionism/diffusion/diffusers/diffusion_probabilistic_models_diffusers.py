from typing import Optional
import torch
from torch import Tensor
from .diffuser import Diffuser
from ..buffers.diffusion_probabilistic_models_buffer import DiffusionProbabilisticModelsBuffer


class DiffusionProbabilisticModelsDiffuser(Diffuser, buffer=DiffusionProbabilisticModelsBuffer):
    diffusion_buffer: DiffusionProbabilisticModelsBuffer
    
    @classmethod
    def diffuse(
        cls,
        diffusion_buffer: DiffusionProbabilisticModelsBuffer,
        input_start: Tensor,
        timestep: Tensor,
        *args,
        degradation: Optional[Tensor] = None,
        **kwargs
    ) -> Tensor:
        # q_sample
        if degradation is None:
            degradation = cls.degrade(diffusion_buffer, input_start, timestep, *args, **kwargs)
        mean = diffusion_buffer.retention_total_std(input_start, timestep, *args, **kwargs) * input_start
        std = diffusion_buffer.degradation_total_std(input_start, timestep, *args, **kwargs)
        x_t = mean + std * degradation
        return x_t
    
    @classmethod
    def degrade(
        cls,
        diffusion_buffer: DiffusionProbabilisticModelsBuffer,
        input: Tensor,
        timestep: Tensor,
        *args,
        **kwargs
    ) -> Tensor:
        return torch.randn_like(input)