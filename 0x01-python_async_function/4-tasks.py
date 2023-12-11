#!/usr/bin/env python3
"""
Function that's similar to wait_n from 1-concurrent_coroutines.py but uses
task_wait_random instead of wait_random
"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """
    function that gets n sorted random delays up to max_delay
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
