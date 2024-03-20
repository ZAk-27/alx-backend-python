#!/usr/bin/env python3
'''Task 1 documentation.
'''
from typing import List
from importlib import import_module as using


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''Creating the list.
    '''
    return [nmb async for nmb in async_generator()]
