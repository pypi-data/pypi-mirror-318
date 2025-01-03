from enum import Enum
from typing import Callable, Any, Iterable
from joblib import Parallel, delayed as joblib_delayed
import dask.distributed
from tqdm import tqdm
import logging
import math

logger = logging.getLogger(__name__)


class ExecutionMode(Enum):
    SEQUENTIAL = "sequential"
    JOBLIB = "joblib"
    DASK = "dask"


class TaskExecutor:
    """Handles task execution using different backends (sequential, joblib, or dask)"""

    def __init__(
        self,
        mode: ExecutionMode = ExecutionMode.SEQUENTIAL,
        n_jobs: int = 1,
        dask_client: dask.distributed.Client = None,
        batch_size: int = 1000,
        **kwargs,
    ):
        self.mode = mode
        self.n_jobs = n_jobs
        self.dask_client = dask_client
        self.batch_size = batch_size
        self.kwargs = kwargs
        logger.debug(f"Initialized TaskExecutor with mode={mode}, n_jobs={n_jobs}")
        if dask_client:
            logger.debug(
                f"Using dask client with dashboard at {dask_client.dashboard_link}"
            )

    def _process_dask_batch(self, func, items):
        """Process a batch of items using dask"""
        futures = []
        for item in items:
            future = self.dask_client.submit(func, item)
            futures.append(future)
        return self.dask_client.gather(futures)

    def map(
        self,
        func: Callable,
        items: Iterable[Any],
        show_progress: bool = True,
    ) -> list:
        """Execute function across items using specified execution mode"""
        items = list(items)  # Convert to list to get length
        logger.debug(
            f"Mapping {func.__name__} across {len(items)} items using {self.mode.value} mode"
        )

        if self.mode == ExecutionMode.SEQUENTIAL:
            logger.debug("Using sequential processing")
            if show_progress:
                return [func(item) for item in tqdm(items)]
            return [func(item) for item in items]

        elif self.mode == ExecutionMode.JOBLIB:
            logger.debug(f"Using joblib with {self.n_jobs} workers")
            if show_progress:
                return Parallel(n_jobs=self.n_jobs, **self.kwargs)(
                    joblib_delayed(func)(item) for item in tqdm(items)
                )
            return Parallel(n_jobs=self.n_jobs, **self.kwargs)(
                joblib_delayed(func)(item) for item in items
            )

        elif self.mode == ExecutionMode.DASK:
            if self.dask_client is None:
                raise ValueError("Dask client must be provided when using dask mode")
            
            total_items = len(items)
            num_batches = math.ceil(total_items / self.batch_size)
            logger.debug(f"Processing {total_items} items in {num_batches} batches")
            
            results = []
            with tqdm(total=total_items, disable=not show_progress) as pbar:
                for i in range(0, total_items, self.batch_size):
                    batch = items[i:i + self.batch_size]
                    logger.debug(f"Processing batch {i//self.batch_size + 1}/{num_batches} with {len(batch)} items")
                    
                    batch_results = self._process_dask_batch(func, batch)
                    results.extend(batch_results)
                    pbar.update(len(batch))
            
            return results

        else:
            raise ValueError(f"Unknown execution mode: {self.mode}")


def process_tile_chunk(chunk_data):
    """Standalone function for processing tile chunks that can be pickled"""
    func = chunk_data['func']
    args = chunk_data.get('args', [])
    kwargs = chunk_data.get('kwargs', {})
    return func(*args, **kwargs)
