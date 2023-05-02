#!/usr/bin/env python3
"""This function takes two arguments,
n and max_delay, and returns a list of floats.
It first creates a list of n tasks, where each
task is a coroutine returned by the task_wait_random
function with max_delay as its argument.
Then, it waits for all the tasks to complete
using asyncio.as_completed which returns an
iterator that yields completed futures.
Finally, it gets the results of all the
completed tasks and returns the list of
results."""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Create a list of n tasks, each task is a coroutine
     returned from task_wait_random function"""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    
    '''Wait for all tasks to complete and get their results'''
    results = [await task for task in asyncio.as_completed(tasks)]
    
    '''Return the list of results'''
    return results