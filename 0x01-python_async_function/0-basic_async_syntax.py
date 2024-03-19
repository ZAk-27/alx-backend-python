#!/usr/bin/env python3
'''Task 0 documnttation.
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''Waiting a random number of seconds.
    '''
    waitime = random.random() * max_delay
    await asyncio.sleep(waitime)
    return waitime
