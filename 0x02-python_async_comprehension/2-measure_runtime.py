#!/usr/bin/env python3
"""Run time for four parallel comprehensions"""

import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Define an asynchronous function to measure
    the total runtime of four executions of
    async_comprehension

    Returns:
        float: _description_
    """
    start_time = time.time()

    tasks = []
    for i in range(4):
        tasks.append(asyncio.ensure_future(async_comprehension()))

    await asyncio.gather(*tasks)

    end_time = time.time()
    return end_time - start_time
