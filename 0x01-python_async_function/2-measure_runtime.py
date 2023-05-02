#!/usr/bin/env python3
""" 
Create a measure_time function with integers n
and max_delay as arguments that measures the
total execution time for wait_n(n, max_delay),
and returns total_time / n.
Your function should return a float."""

from time import perf_counter
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Define a function to measure the time taken
     to execute concurrent coroutines"""

    ''' Get the start time'''
    start = perf_counter()
    
    '''Run the coroutines concurrently'''
    asyncio.run(wait_n(n, max_delay))
    
    '''Calculate the total_time'''
    total_time  = perf_counter() - start
    
    '''Return the average time per coroutine'''
    return total_time  / n