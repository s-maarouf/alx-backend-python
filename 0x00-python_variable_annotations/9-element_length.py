#!/usr/bin/env python3

"""type annonated module"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns appropriate types"""
    return [(i, len(i)) for i in lst]
