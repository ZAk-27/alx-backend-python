#!/usr/bin/env python3
'''doc style.
'''
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''doc style.
    '''
    if lst:
        return lst[0]
    else:
        return None
