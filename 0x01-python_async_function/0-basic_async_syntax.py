#!/usr/bin/env python3

"""Async coroutine module"""


import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """an asynchronous coroutine that waits for a random delay
    between 0 and max_delay"""
    waiting = random.random() * max_delay
    await asyncio.sleep(waiting)
    return waiting
