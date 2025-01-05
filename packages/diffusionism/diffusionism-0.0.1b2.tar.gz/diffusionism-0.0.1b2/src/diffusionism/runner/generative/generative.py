from typing import Callable, Optional, Tuple, Union, Iterable, Mapping, Dict, Sequence
import numpy as np
import torch
import torchflint as te
from ..model_runner import ModelRunner


class GenerativeRunner(ModelRunner):
    def __init__(
        self,
        target_data_getter: Callable[[Tuple[torch.Tensor, ...]], Tuple[torch.Tensor, ...]],
        source_data_getter: Optional[Callable[[Tuple[torch.Tensor, ...]], Tuple[torch.Tensor, ...]]] = None,
        data_getter: Optional[Callable[[Tuple[torch.Tensor, ...]], Tuple[torch.Tensor, ...]]] = None,
        *args,
        metrics: Union[Callable[[torch.Tensor], torch.Tensor], Iterable[Callable[[torch.Tensor], torch.Tensor]], None] = None,
        global_metrics: Union[Callable[[torch.Tensor], torch.Tensor], Iterable[Callable[[torch.Tensor], torch.Tensor]], None] = None,
        **kwargs
    ):
        """
        Args:
            target_data_getter (Callable[[Tuple[torch.Tensor, ...]], Tuple[torch.Tensor, ...]]):
                The target input data for the diffusion.
            source_data_getter (Optional[Callable[[Tuple[torch.Tensor, ...]], Tuple[torch.Tensor, ...]]]):
                The source data that may be used to translate the source data into the target data.
                If ``None``, no translation task will be runned.
            data_getter (Optional[Callable[[Tuple[torch.Tensor, ...]], Tuple[torch.Tensor, ...]]]): The
                data that is not regarding to the direct diffusion, but may be for guidance. If ``None``,
                no other data will be used.
            metrics (Union[Callable[[torch.Tensor], torch.Tensor], Iterable[Callable[[torch.Tensor], torch.Tensor]], None]):
                The metrics list that contains all metrics calculation function, used after each validation and test step.
            global_metrics (Union[Callable[[torch.Tensor], torch.Tensor], Iterable[Callable[[torch.Tensor], torch.Tensor]], None]):
                The metrics list that contains all metrics calculation function, used in generated distribution
                and the original distribution. When it is not ``None`` or empty, generation collection will be
                automatically available to obtain.
        
        """
        super().__init__(*args, **kwargs)
        self.__test_collection = self.__validation_collection = None
        self.__generation = self.__target = None
        
        self.target_data_getter = target_data_getter
        self.source_data_getter = source_data_getter
        self.data_getter = data_getter
        
        if metrics is None:
            self.metrics = []
        elif isinstance(metrics, Sequence):
            self.metrics = metrics
        else:
            self.metrics = [metrics]
        if global_metrics is None:
            self.global_metrics = []
        elif isinstance(global_metrics, Sequence):
            self.global_metrics = global_metrics
        else:
            self.global_metrics = [global_metrics]
    
    def get_target_data(self, batch):
        return self.target_data_getter(batch)
    
    def get_source_data(self, batch):
        if self.source_data_getter is None:
            return tuple()
        else:
            data = self.source_data_getter(batch)
            if not isinstance(data, tuple):
                data = (data,)
            return data
    
    def get_additional_data(self, batch):
        if self.data_getter is None:
            return tuple()
        else:
            data = self.data_getter(batch)
            if not isinstance(data, tuple):
                data = (data,)
            return data
    
    def process_training_step_mean_metrics(self, loss):
        self.log('Loss', loss, prog_bar=True, logger=True, on_step=True, on_epoch=True)
        # self.log("Global Step", self.global_step, prog_bar=True, logger=False, on_step=True, on_epoch=False)
    
    # def end_for_training_epoch(self, losses: torch.Tensor):
    #     self.log('Epoch Loss', losses.mean(), prog_bar=True, logger=True, on_step=False, on_epoch=True)
    #     # self.log('Epoch', self.current_epoch, prog_bar=True, logger=True, on_step=False, on_epoch=True)
    
    def generate(self, batch, batch_idx, source_input: Tuple[torch.Tensor, ...], data: Tuple[torch.Tensor, ...], target_input: Optional[torch.Tensor] = None) -> torch.Tensor:
        pass
    
    @torch.inference_mode()
    def __evaluation_step(self, batch, batch_idx, log_prefix = None, return_images: bool = False) -> Mapping[str, torch.Tensor]:
        """Evaluates the batch step.

        Args:
            batch: The output of your data iterable, normally a :class:`~torch.utils.data.DataLoader`.
            batch_idx: The index of this batch.
            log_prefix (Optional[str]): The string that tells the evaluation type, for example, 'val' or 'test'.
            return_images (bool): The flag that controls whether adding the sampled and original images into
                the returned dictionary.

        Returns:
            Mapping: A dictionary that contains all metrics and the images if
                :param:`return_images` is ``True``.
        
        """
        target_input: torch.Tensor = self.get_target_data(batch)
        generation = self.generate(batch, batch_idx, self.get_source_data(batch), self.get_additional_data(batch), target_input)
        map_dim = tuple(np.arange(1, len(target_input.shape)))
        target_input = te.map_range(target_input, dim=map_dim)
        generation = te.map_range(generation, dim=map_dim)
        metric_values = {type(metric).__name__ : metric(generation, target_input) for metric in self.metrics}
        if log_prefix is None:
            collection_dict = metric_values
        else:
            collection_dict = {f'{log_prefix}-{key}' : value for key, value in metric_values.items()}
        if len(collection_dict) > 0:
            # self.log_dict(collection_dict, prog_bar=False, logger=False, on_step=True, on_epoch=True)
            self.log_dict({key : value.mean() for key, value in collection_dict.items()}, prog_bar=True, logger=True, on_step=False, on_epoch=True)
        if return_images:
            return metric_values, generation, target_input
        return metric_values
    
    # @torch.no_grad()
    # def evaluation_epoch_end(self, outputs: List[Dict[str, torch.Tensor]], need_clear: bool = True) -> Mapping[str, torch.Tensor]:
    #     """Gives the evaluation results of the whole dataset after all steps are evaluated, reaching
    #     to the epoch end.

    #     Args:
    #         outputs (List[Dict[str, torch.Tensor]]): The output list containing all step results.
    #         need_clear (bool): A flag that determines whether clearing the outputs list.

    #     Returns:
    #         Mapping: A dictionary that is gathered from the output list.
        
    #     """
    #     keys = set()
    #     for dictionary in outputs:
    #         keys = keys.union(set(dictionary.keys()))
    #     output_dict = outputs[0]
    #     for output in outputs[1:]:
    #         for key in keys:
    #             key_output = output.get(key)
    #             key_result_output = output_dict.get(key)
    #             if key_result_output is not None:
    #                 if not isinstance(key_result_output, list):
    #                     output_dict[key] = [key_result_output]
    #                 if key_output is not None:
    #                     output_dict[key].append(key_output)
    #             elif key_output is not None:
    #                 output_dict[key] = [key_output]
    #     for key in keys:
    #         output_dict[key] = torch.vstack(output_dict[key]).mean()
    #     if need_clear:
    #         outputs.clear()
    #     return output_dict
    
    @torch.no_grad()
    def validate_at_step(self, batch, batch_idx) -> Union[torch.Tensor, Tuple[torch.Tensor, ...]]:
        need_images = self.__validation_collection is not None or len(self.global_metrics) > 0
        metric_values = self.__evaluation_step(batch, batch_idx, log_prefix='Val', return_images=need_images)
        if need_images:
            if self.__validation_collection is None:
                self.need_validation_results()
            metric_values, generation, target = metric_values
            self.__validation_collection[0].append(generation)
            self.__validation_collection[1].append(target)
        return metric_values
    
    def end_for_validation_epoch(self, outputs: dict[str, torch.Tensor]):
        log = {key : value.mean() for key, value in outputs.items()}
        if len(self.global_metrics) > 0:
            generation, target = self.__concat_collection(self.__validation_collection)
            log.update({f'Val-{type(metric).__name__}_epoch' : metric(generation, target).mean() for metric in self.global_metrics})
        if len(log) > 0:
            self.log_dict(log, prog_bar=False, logger=True, on_step=False, on_epoch=True)
    
    @torch.no_grad()
    def test_at_step(self, batch, batch_idx) -> Union[torch.Tensor, Tuple[torch.Tensor, ...]]:
        need_images = self.__test_collection is not None or len(self.global_metrics) > 0
        metric_values = self.__evaluation_step(batch, batch_idx, log_prefix='Val', return_images=need_images)
        if need_images:
            if self.__test_collection is None:
                self.need_test_results()
            metric_values, generation, target = metric_values
            self.__test_collection[0].append(generation)
            self.__test_collection[1].append(target)
        return metric_values
    
    def end_for_test_epoch(self, outputs: dict[str, torch.Tensor]):
        log = {key : value.mean() for key, value in outputs.items()}
        if len(self.global_metrics) > 0:
            generation, target = self.__concat_collection(self.__test_collection)
            log.update({f'Test-{type(metric).__name__}_epoch' : metric(generation, target).mean() for metric in self.global_metrics})
        if len(log) > 0:
            self.log_dict(log, prog_bar=False, logger=True, on_step=False, on_epoch=True)
    
    def __concat_collection(self, collection) -> Tuple[torch.Tensor, torch.Tensor]:
        if self.__generation is None:
            generation, target = collection[0], collection[1]
            generation = torch.concat(generation, dim=0).permute(0, 2, 3, 1)
            target = torch.concat(target, dim=0).permute(0, 2, 3, 1)
            self.__generation = generation
            self.__target = target
        return self.__generation, self.__target
        
    def __evaluation_results(self, results, collection) -> Union[torch.Tensor, Tuple[torch.Tensor, ...], Dict[str, torch.Tensor]]:
        if collection is not None:
            generation, target = self.__concat_collection(collection)
            error_map = torch.abs(generation - target)
            if isinstance(results, tuple):
                results = results + (generation, target, error_map)
            elif isinstance(results, dict):
                results.update({
                    'generation' : generation,
                    'target' : target,
                    'error' : error_map
                })
            else:
                results = results, generation, target, error_map
        return results
    
    def need_validation_results(self, need = True, need_images = True, *args, **kwargs):
        """Informs the runner to store the validation results, and collect them later by using
        :attr:`take_validation_results`.

        Args:
            need (bool): The flag that controls whether to use the validation results.
            need_images (bool) : The flag that controls whether to use the validation images.
        
        """
        super().need_validation_results(need, *args, **kwargs)
        if need_images:
            self.__generation = self.__target = None
            self.__validation_collection = ([], [])
        else:
            self.__validation_collection = None
    
    @property
    def __validation_results__(self) -> Union[torch.Tensor, Tuple[torch.Tensor, ...], Dict[str, torch.Tensor]]:
        return self.__evaluation_results(super().__validation_results__, self.__validation_collection)
    
    def take_validation_results(self) -> Union[Tuple[torch.Tensor, ...], Tuple[Dict[str, torch.Tensor], torch.Tensor, torch.Tensor]]:
        result = super().take_validation_results()
        self.__generation = self.__target = self.__validation_collection = None
        return result
    
    def need_test_results(self, need = True, need_images = True, *args, **kwargs):
        """Informs the runner to store the test results, and collect them later by using
        :attr:`take_test_results`.

        Args:
            need (bool): The flag that controls whether to use the test results.
            need_images (bool) : The flag that controls whether to use the test images.
        
        """
        super().need_test_results(need, *args, **kwargs)
        if need_images:
            self.__generation = self.__target = None
            self.__test_collection = ([], [])
        else:
            self.__test_collection = None
    
    @property
    def __test_results__(self) -> Union[torch.Tensor, Tuple[torch.Tensor, ...], Dict[str, torch.Tensor]]:
        return self.__evaluation_results(super().__test_results__, self.__test_collection)
    
    def take_test_results(self) -> Union[Tuple[torch.Tensor, ...], Tuple[Dict[str, torch.Tensor], torch.Tensor, torch.Tensor]]:
        result = super().take_test_results()
        self.__generation = self.__target = self.__test_collection = None
        return result