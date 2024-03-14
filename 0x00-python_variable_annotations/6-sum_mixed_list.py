#!/usr/bin/env python3

"""type annonated module"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns sum of mixed list"""
    return float(sum(mxd_lst))
