
from typing import Any, Callable, Optional
from functools import wraps

from .helpers.classes import Data
from .helpers.main_helper import normalize_args_kwargs

from pprint_tree import pprint_tree

def show_recursion_tree(func):

    Data.reset()

    def wrapper(*args, **kwargs) -> Any:

        norm_args: str = normalize_args_kwargs(args, kwargs)

        Data.push(norm_args)
        func_output = func(*args, **kwargs)
        node = Data.pop(func_output)

        if not Data.stack:
            # only when stack is empty, we know this is the root node
            print()
            pprint_tree(node)

        return func_output
    
    return wrapper
    