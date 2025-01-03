from enum import Enum
from typing import Callable, Any, Iterable
from joblib import Parallel, delayed as joblib_delayed
import dask.distributed
import dask.bag as db
from dask import delayed
from tqdm import tqdm
import logging
import math

logger = logging.getLogger(__name__)

# Move process_item outside the class to make it pickleable
@delayed
def _process_dask_item(func, item):
    try:
        logger.debug(f"Processing item in Dask worker")
        result = func(item)
        logger.debug(f"Successfully processed item")
        return result
    except Exception as e:
        logger.error(f"Error processing item: {str(e)}", exc_info=True)
        raise

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
        logger.info(f"Initialized TaskExecutor with mode={mode}, n_jobs={n_jobs}")
        if dask_client:
            logger.info(f"Using dask client with dashboard at {dask_client.dashboard_link}")
            logger.debug(f"Dask client kwargs: {kwargs}")

    def map(
        self,
        func: Callable,
        items: Iterable[Any],
        show_progress: bool = True,
    ) -> list:
        items = list(items)
        logger.info(f"Starting map operation with {len(items)} items using {self.mode.value} mode")
        logger.debug(f"Function to map: {func.__name__}")

        if self.mode == ExecutionMode.SEQUENTIAL:
            logger.info("Using sequential processing")
            if show_progress:
                return [func(item) for item in tqdm(items)]
            return [func(item) for item in items]

        elif self.mode == ExecutionMode.JOBLIB:
            logger.info(f"Using joblib with {self.n_jobs} workers")
            logger.debug(f"Joblib kwargs: {self.kwargs}")
            if show_progress:
                return Parallel(n_jobs=self.n_jobs, **self.kwargs)(
                    joblib_delayed(func)(item) for item in tqdm(items)
                )
            return Parallel(n_jobs=self.n_jobs, **self.kwargs)(
                joblib_delayed(func)(item) for item in items
            )

        elif self.mode == ExecutionMode.DASK:
            if self.dask_client is None:
                logger.error("No Dask client provided")
                raise ValueError("Dask client must be provided when using dask mode")

            logger.info("Setting up Dask computation")
            
            # Create futures directly instead of using dask.bag
            futures = []
            for item in items:
                future = self.dask_client.submit(_process_dask_item, func, item)
                futures.append(future)
            
            # Compute with progress tracking
            total_items = len(items)
            logger.info(f"Starting computation of {total_items} items")
            with tqdm(total=total_items, disable=not show_progress) as pbar:
                try:
                    logger.debug("Starting Dask computation")
                    results = self.dask_client.gather(futures)
                    logger.debug("Completed Dask computation")
                    for _ in results:
                        pbar.update(1)
                    
                    logger.info("Successfully completed all computations")
                    return results
                except Exception as e:
                    logger.error(f"Error during Dask computation: {str(e)}", exc_info=True)
                    raise

        else:
            logger.error(f"Invalid execution mode: {self.mode}")
            raise ValueError(f"Unknown execution mode: {self.mode}")
