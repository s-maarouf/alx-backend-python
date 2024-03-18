#!/usr/bin/env python3

"""async coroutine module"""

from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """a routine that returns the list of all the delays"""
    waiting = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(waiting)
