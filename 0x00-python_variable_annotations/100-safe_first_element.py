#!/usr/bin/env python3
"""
    Given the parameters and the return values,
    add type annotations to the function

"""
from typing import Any, Union, Sequence

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    if lst:
        return lst[0]
    else:
        return None
