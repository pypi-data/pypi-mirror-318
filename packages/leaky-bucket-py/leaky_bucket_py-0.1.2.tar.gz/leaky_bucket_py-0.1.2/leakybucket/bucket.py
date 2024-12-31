import time
import asyncio
from .persistence.base import BaseLeakyBucketStorage

_current_task = asyncio.current_task

class LeakyBucket:
    """
    A simple synchronous leaky bucket that
    delegates to a (sync-friendly) storage backend.
    """

    def __init__(self, storage_backend: BaseLeakyBucketStorage):
        self._storage = storage_backend

    def acquire(self, amount: float = 1.0):
        """
        Acquire the requested amount of capacity from the bucket.
        This can be called explicitly, or used as a context manager.
        """
        if amount > self._storage.max_level:
            raise ValueError("Cannot acquire more than the bucket capacity")

        while not self._storage.has_capacity(amount):
            # simple sleep roughly for the drip interval:
            time.sleep(1 / self._storage.rate_per_sec * amount)
        self._storage.increment_level(amount)

    def __enter__(self):
        self.acquire()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return None


class AsyncLeakyBucket:
    """
    An async leaky bucket that delegates storage to a BaseLeakyBucketStorage implementation.
    """

    def __init__(self, storage_backend: BaseLeakyBucketStorage):
        self._storage = storage_backend

    async def acquire(self, amount: float = 1.0) -> None:
        """
        Acquire the requested amount of capacity from the bucket.
        This can be called explicitly, or used as an async context manager.
        """
        loop = asyncio.get_event_loop()
        task = _current_task(loop)
        if amount > self._storage.max_level:
            raise ValueError("Cannot acquire more than the bucket capacity")

        while not self._storage.has_capacity(amount):
            fut = loop.create_future()
            self._storage.add_waiter(task, fut)
            try:
                # Wait for capacity or time out after ~the drip interval
                await asyncio.wait_for(
                    asyncio.shield(fut),
                    1 / self._storage.rate_per_sec * amount,
                )
            except asyncio.TimeoutError:
                pass
            finally:
                self._storage.remove_waiter(task)
        self._storage.increment_level(amount)

    async def __aenter__(self):
        await self.acquire()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        return None