from enum import Enum
from typing import Callable, Any, Iterable
from joblib import Parallel, delayed
import dask.distributed
from tqdm import tqdm
from dask.distributed import progress as dask_progress
import logging

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
        **kwargs,
    ):
        self.mode = mode
        self.n_jobs = n_jobs
        self.dask_client = dask_client
        self.kwargs = kwargs
        logger.debug(f"Initialized TaskExecutor with mode={mode}, n_jobs={n_jobs}")
        if dask_client:
            logger.debug(
                f"Using dask client with dashboard at {dask_client.dashboard_link}"
            )

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
                    delayed(func)(item) for item in tqdm(items)
                )
            return Parallel(n_jobs=self.n_jobs, **self.kwargs)(
                delayed(func)(item) for item in items
            )

        elif self.mode == ExecutionMode.DASK:
            if self.dask_client is None:
                raise ValueError("Dask client must be provided when using dask mode")

            logger.debug("Submitting tasks to dask cluster")
            futures = self.dask_client.map(func, items)
            if show_progress:
                dask_progress(futures)

            logger.debug("Gathering results from dask cluster")
            results = self.dask_client.gather(futures)
            logger.debug("Finished gathering results")
            return results

        else:
            raise ValueError(f"Unknown execution mode: {self.mode}")
