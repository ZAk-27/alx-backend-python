#!/usr/bin/env python3
""" documentation task 4"""
import asyncio
import random
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """documentation"""
    waitimes = []
    for _ in range(n):
        waitimes.append(task_wait_random(max_delay))
    return sorted(await asyncio.gather(*waitimes))
