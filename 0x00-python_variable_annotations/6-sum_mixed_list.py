#!/usr/bin/env python3
"""
Type-annotated function that takes a list of floats and ints and returns sum
"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    sum of items of list
    """
    return (sum(mxd_list))
