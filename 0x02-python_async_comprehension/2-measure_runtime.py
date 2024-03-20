#!/usr/bin/env python3
'''Task 2 documentation.
'''
import asyncio
import time
from importlib import import_module as using


async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Executing async_comprehension 4 times..
    '''
    startime = timend()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return timend() - startime
