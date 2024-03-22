#!/usr/bin/env python3
"""
spawning wait_random function n times
"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all the delays """
    delays = []
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    for task in tasks:
        delay = await task
        delays.append(delay)

    return sorted(delays)
