#!/usr/bin/env python3
"""
Function that returns the execution time for wait_n
"""
import asyncio
from time import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int = 0, max_delay: int = 10) -> float:
    """
    Returns the execution time for wait_n
    """
    start = time()
    asyncio.run(wait_n(n, max_delay))
    total = time() - start
    return (total / n)
