#!/usr/bin/env python3
"""
measure_runtime measures time it takes async_comprehension to run four times
in parellel
"""
import asyncio
from time import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measures runtime of async_comprehenion running 4 times in parellel
    """
    start = time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end = time()
    runtime = end - start
    return runtime
