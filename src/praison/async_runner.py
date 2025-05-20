"""Async execution engine for parallel agent tasks."""

import asyncio
from typing import List, Callable

class AsyncRunner:
    def __init__(self, max_concurrent: int = 5):
        self.max_concurrent = max_concurrent
        self.semaphore = asyncio.Semaphore(max_concurrent)
    
    async def run_parallel(self, tasks: List[Callable]):
        async def bounded_task(task):
            async with self.semaphore:
                return await task()
        return await asyncio.gather(*[bounded_task(t) for t in tasks])
