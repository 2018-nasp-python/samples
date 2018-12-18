#!/usr/bin/env python3

"""
This script demonstrates the use of default parameter values.
"""

def func_w_default_arg_values(arg1=10, arg2=10):
    return arg1 * arg2


def func_w_default_mutable_arg_bad(height, width, description=[]):
    description.append(height)
    description.append(width)
    description.append(width * height)

    return description


def func_w_default_mutable_arg(height, width, description=None):
    if description is None:
        description = []
    description.append(height)
    description.append(width)
    description.append(width * height)

    return description


if __name__ == '__main__':
    print(func_w_default_arg_values())
    print(func_w_default_arg_values(1))
    print(func_w_default_arg_values(2, 3))

    info_list_1 = ["square1", "value1"]
    print(func_w_default_mutable_arg_bad(2, 2))
    print(func_w_default_mutable_arg_bad(3, 3))
    print(func_w_default_mutable_arg_bad(2, 2, info_list_1))

    info_list_2 = ["square2", "value2"]
    print(func_w_default_mutable_arg(2, 2))
    print(func_w_default_mutable_arg(3, 3))
    print(func_w_default_mutable_arg(2, 2, info_list_2))
