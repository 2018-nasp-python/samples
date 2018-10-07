#! /usr/bin/env python3
"""Demontrate range function by looping through three ranges
"""

# generate a sequence of numbers from zero up to but not including the
# specified number.
for counter in range(10):
    print(counter)

# generate a sequence of numbers from starting number up to but not including
# the specified ending number.
for counter in range(10, 16):
    print(counter)

# generate a sequence of numbers from starting number up to but not including
# the specified ending number counting in increments of the specified step.
for counter in range(7, 100, 7):
    print(counter)
