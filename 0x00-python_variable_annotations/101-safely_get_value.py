#!/usr/bin/env python3
"""
        Use mypy to validate the following piece of
        code and apply any necessary changes.

"""

from typing import Mapping, Any, Union, TypeVar, Optional

T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: 
            Optional[T] = None) -> Union[Any, T]:
    """ 
    Define a function that takes a dictionary `dct`,
    a key `key`, and an optional default value `default`
     
     The type annotations are `Mapping` for `dct`,
     `Any` for `key`, `Optional[T]` for `default`,
     and `Union[Any, T]` for the return type
     """

    if key in dct:  # Check if the key is in the dictionary
        return dct[key]  # If so, return the value associated with the key
    else:
      """ Otherwise, return the default value 
          (or None if no default is provided)
     """
    return default  
    
