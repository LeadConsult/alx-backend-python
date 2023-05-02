#!/usr/bin/env python3
"""
A type-annotated function make_multiplier
that takes a float multiplier as argument and
returns a function that multiplies a float by
multiplier.

"""

import typing

def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    if True:
        def float_multiplier(product : float) -> float:
            return multiplier * product 

        return float_multiplier
