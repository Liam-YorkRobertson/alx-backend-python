#!/usr/bin/env python3
"""
Type-annotated function that multiplies a float by a multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a float multiplied by a specified multiplier
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function