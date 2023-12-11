#!/usr/bin/env python3
"""
Function that runs wait_random n amoutn of times and returns values in a list
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int = 0, max_delay: int = 10) -> list[float]:
    """
    function that gets n sorted random delays up to max_delay
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
