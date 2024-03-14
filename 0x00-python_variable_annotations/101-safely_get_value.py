#!/usr/bin/env python3

"""type annonated module"""

from typing import Union, Any, Mapping, TypeVar


T = TypeVar('T')
res = Union[Any, T]
deft = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: deft = None) -> res:
    """returns a value from a dict using a given key"""
    if key in dct:
        return dct[key]
    else:
        return default
