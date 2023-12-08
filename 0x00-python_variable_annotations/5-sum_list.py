#!/usr/bin/env python3
"""
Type-annotated function that takes a list of floats and returns the sum
"""
from typing import List


def sum_list(input_list: float = List) -> float:
    """
    sum of items of list
    """
    return (sum(input_list))
