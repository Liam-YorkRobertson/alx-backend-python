#!/usr/bin/env python3
"""
Function that loops and yields a random number
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Function that loops 10 times, waits then returns a random number
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
