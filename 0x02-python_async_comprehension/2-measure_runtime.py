#!/usr/bin/env python3
'''Task 2 documentation.
'''
import asyncio
import time
from importlib import import_m















#!/usr/bin/env python3
""" doc task 2 """
import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """ documentation task 2"""
    start = startime.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension()
                         )
    end = timend.perf_counter()
    return end - start
