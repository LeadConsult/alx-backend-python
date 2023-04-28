#!/usr/bin/env python3
"""
Use mypy to validate the following piece
of code and apply any necessary changes.
"""
# Importing necessary modules
from typing import Tuple, List

""" Defining a function zoom_array that takes a tuple
and an integer as inputs, and returns a list"""
def zoom_array(lst: Tuple, factor: int = 2) -> List:
    
    """ Initializing an empty list named zoomed_in and
    filling it with the original items multiplied by factor"""
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    """ Returning the zoomed_in list """
    return zoomed_in

""" Defining a tuple named array """
array: Tuple = (12, 72, 91)

""" Creating a new list named zoom_2x using
the zoom_array function and the array tuple
with default factor value 2
"""
zoom_2x = zoom_array(array)

""" Creating another new list named zoom_3x
using the zoom_array function and the array
tuple with factor value 3"""
zoom_3x = zoom_array(array, 3)
