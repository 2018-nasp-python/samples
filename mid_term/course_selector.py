#! /usr/bin/env python3
"""
This module builds a program workload for a general interest computing
program.  Courses are selected from a course catalogue.

Being a general interest continuing studies program and there are no program
requirements either in number of, ordering, or specific required courses.

Once a user has completed course selections. the total program hours are
calculated based on the number of credits in each course.  Each credit is
comprised of 14 hours of course work.

From the required hours the number of semesters is calculated based on a
semester length of 120 hours for part time studies and 360 hours for full time
studies.

The courses selected and the number of semesters required to finish the program
is printed for the user.

"""

import math
from typing import List, Dict

calendar: Dict[str, float] = {
    "CS101": 6.00,
    "CS102": 6.00,
    "CS103": 5.00,
    "CS104": 5.00,
    "MA101": 4.00,
    "MA102": 4.00,
    "CO101": 3.00,
    "CO102": 3.00,
    "OR101": 3.00,
    "OR102": 3.00
}
""" Maps course code to the number of credits
"""


CREDIT_HOURS = 14
""" Constant storing the number of hours per course
"""


delivery_type: Dict[str, float] = {"pt": 120,
                                   "ft": 360}
""" Maps delivery code to hours per semester
"""


def course_hours(course: str) -> float:
    """
    Calculate the number of hours to complete a given course

    Args:
        course (str): the name of the course

    Returns:
        (float): the number of hours required to complete the course  
    """

    return calendar[course] * CREDIT_HOURS


def calculate_semesters(workload: List[str], attendance: str) -> int:
    """
    Calculates the number of semester to complete the courseload and attendance

    Based on the students delivery type ("pt" - Part Time or "ft" - Full Time)
    calculate the number of semesters to complete their workload.

    The number of hours in a course is calculated as follows:
        course hours = credits * 14 hours per credit

    The number of hours in a semester is specified as follows:
        pt = 120
        ft = 360

    The number of semesters is calculated as follows:
        (the total hours in program / hours in semester) rounded up to nearest
        whole semester.

    see 'math.ceil' for standard library method of preforming rounding

    Args:
        workload (List[str]): this is a list of course codes that comprise the 
                              students workload

        attendance (str): "pt" or "ft" indicating whether the student will be
                          attending part time or full time

    Returns:
        int: number of semesters to complete workload
    """

    hours = 0.0

    for course in workload:
        hours += course_hours(course)

    semesters = math.ceil(hours / delivery_type[attendance])

    return semesters


def build_program() -> List[str]:
    """
    Prompt the user for courses that they want to enroll in and add them to
    their customized program

    If the courses is not in the course catalogue inform them by printing:
        "Sorry, $course_input isn't currently offered"

    Where $course_input is the course code they entered at the prompt. 

    After a failed input attempt the user will be prompted to input another
    course code. 

    The user will continue to select courses until they enter 'done' when to
    indicate that have finished adding courses.

    Returns:
        (List[str]): a list of courses to in which the student will be
                     enrolled
    """

    course = ""
    program = []

    while course != "done":
        course = input(
            "What course would you like register for - enter 'done' when finished: ")
        if course == "done":
            break
        elif course not in calendar:
            print("Sorry, {} isn't currently offered".format(course))
            continue
        program.append(course)

    return program


def main():
    """
    Build course program and select delivery type, then print the courses and
    completion time in semesters
    """

    program = build_program()
    delivery_method = input(
        "Will you be attending full time(ft) or part time (pt): ")
    semesters = calculate_semesters(program, delivery_method)
    print("Your program includes the following courses:\n{}".format(program))
    print("It will take you {} semesters to complete".format(semesters))


if __name__ == "__main__":
    main()
