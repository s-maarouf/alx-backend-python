#!/usr/bin/env python3

"""async routine module"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """a function that measures the total execution of a function"""
    s_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - s_time) / n
