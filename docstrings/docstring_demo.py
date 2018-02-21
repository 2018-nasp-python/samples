#!/usr/bin/env python3
"""Simple docstring demonstration with annotations

This module explicity invokes doctest when run as a script
"""

def adder(arg1: int, arg2: int) -> int:
    """
    Function that sums two numbers

    Args:
        arg1 (int): first number to be added
        arg2 (int): second number to be added

    Returns:
        Sum (int) of arg1 + arg2

    Examples:

        >>> adder(3, 4)
        7

        >>> adder(2, 2)
        4

        >>> adder(1, 1)
        10

    """

    return int(arg1 + arg2)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    adder(3,4)
