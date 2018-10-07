#! /usr/bin/env python3
"""Demonstrates enumerate and tuples

"""

string1 = "This demonstrates that sequences start at 0"

for position, letter in enumerate(string1):
    print("Position {:2}: Letter {}".format(position, letter))