#!/usr/bin/env python3
""" doc style """
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """doc style"""
    return (k, v**2)
