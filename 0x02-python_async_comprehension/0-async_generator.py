#!/usr/bin/env python3
'''Task 0 doc.
'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''Generating a sequence of 10 numbs.
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random(0, 10)
