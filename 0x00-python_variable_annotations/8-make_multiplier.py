#!/usr/bin/env python3
''' doc style.
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    ''' doc style.
    '''
    return lambda x: x * multiplier
