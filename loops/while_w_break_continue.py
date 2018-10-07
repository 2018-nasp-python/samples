#! /usr/bin/env python3
"""Calculates total of user entered digits that are between 1 and 10
"""

total = 0

while True:
    entry = int(input("Enter a number between 1 and 10 or -999 to exit: "))
    if entry == -999:
        break
    if (entry < 1) or (entry > 10):
        continue
    total += entry

print("The total is {}".format(total))
