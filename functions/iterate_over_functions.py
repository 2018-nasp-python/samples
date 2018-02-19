#!/usr/bin/env python3
import sys
import inspect


def loop_over_functions():
    """
    Iterate over all functions in current module

    Returns:

    """
    current_module = sys.modules[__name__]
    for function_name, function_obj in inspect.getmembers(current_module, inspect.isfunction):
        if function_name != "loop_over_functions":
            function_obj()


def print_hello():
   print("Hello")


def print_goodbye():
    print("Goodbye")


if __name__ == '__main__':
    loop_over_functions()
