#! /usr/bin/env python3
"""Calculate the average of grades list using for...in loop
"""


grades = [60, 65, 70, 80]
total = 0

for grade in grades:
    total += grade

# for info on len() see https://docs.python.org/3/library/functions.html#len
average = total / len(grades) 

print("Average grade: {:.2f}".format(average))