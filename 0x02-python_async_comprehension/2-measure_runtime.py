#!/usr/bin/env python3

"""async coroutine module"""

import asyncio
import time
from importlib import import_module as using
async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measures the total runtime and return it"""

    s_time = time.time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    return time.time() - s_time
