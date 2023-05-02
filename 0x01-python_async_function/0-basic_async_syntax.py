#!/usr/bin/env python3
""" Write an asynchronous coroutine that takes in an integer
argument (max_delay, with a default value of 10) named
wait_random that waits for a random delay between 0
and max_delay (included and float value) seconds and
eventually returns it.

Use the random module. """

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Generate a random number between 0 and max_delay"""
    random = random.uniform(0, max_delay)
    """Wait for the specified amount of time"""
    await asyncio.sleep(random)
    """Return the random number"""
    return random