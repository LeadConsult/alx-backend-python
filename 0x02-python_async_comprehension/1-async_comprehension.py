#!/usr/bin/env python3
""" Async Comprehensions"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
   asynchronously loops over the elements yielded
   by the async generator async_generator() and
   collects them into a list.
    """
    results = [i async for i in async_generator()]
    return results