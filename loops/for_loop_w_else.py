#! /usr/bin/env python3
"""For loop with else used build grade list and calculate average if successful
"""


def get_average(grades):
    total = 0
    average = 0
    success = 1

    for grade in grades:
        if type(grade) != int:
            break
        else:
            total += grade
    else:
        average = total / len(grades)
        success = 0

    return success, average


grades = [80, 70, 90, 80]
grades_w_error = [80, "Invalid", 70, 90]

print(get_average(grades))
print(get_average(grades_w_error))
