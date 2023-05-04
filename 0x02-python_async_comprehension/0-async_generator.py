#!/usr/bin/env python3
"""Async Generator"""

import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    The function loops 10 times using the for loop,
    and await the asyncio.sleep(1) coroutine each
    time to pause the execution for 1 second
    before yielding the next value using the yield keyword
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)