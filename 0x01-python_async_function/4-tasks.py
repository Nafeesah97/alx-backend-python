#!/usr/bin/env python3
"""
importing necessary libraries
"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all the delays """
    delays = []
    tasks = [asyncio.create_task(task_wait_random(max_delay)) for _ in range(n)]

    for task in tasks:
        delay = await task
        delays.append(delay)

    return sorted(delays)