#!/usr/bin/env python3
"""
importing necessary libraries
Author: Nafeesah
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """waits for random delay and return it"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
