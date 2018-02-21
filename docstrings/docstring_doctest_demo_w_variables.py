#!/usr/bin/env python3

"""
This script demonstrates the use of docstrings and annotations

It imports the json module for use in loading a grades file.

Also not the creation of variables for use in doctest and the use of doctest
directives.

"""
import json
import os

def demo():

    """
    Demonstrates use of get_course_averages and get_student_grades functions.

    Note the use of doctest directives in the example section.

    Examples:
        >>> demo() #doctest: +NORMALIZE_WHITESPACE
        A00986924 grades: {'ACIT1420': 89, 'ACIT1515': 52, 'ACIT1620': 55,
        'ACIT1630': 46, 'COMM1116': 58, 'MATH1310': 92, 'ORGB1100': 73}
        ORGB1100 average: 72.542
    """
    dir_path = os.path.dirname(os.path.abspath(__file__))
    grades_path = os.path.join(dir_path, "grades.json")
    with open(grades_path, "r") as grades_file:
        grades = json.load(grades_file)

    course_averages = get_course_averages(grades)
    student_grades = get_student_grades(grades)

    print("A00986924 grades: " + str(student_grades["A00986924"]))
    print("ORGB1100 average: " + '{0:.3f}'.format(course_averages["ORGB1100"]))


def get_course_averages(grades: list) -> dict:
    """
    Converts a list containing student ID, course, and grade to a dictionary
    of courses holding a list of average grades

    This also demonstrates the creation of variable using doctest.

    Args:
        grades: this is a list of student ID, course, and grade received

    Returns:
        A dictionary indexed by course code storing the average grade for the
        course

    Examples:

        >>> example_grades = [['A00050346', 'ACIT1420', 51],
        ...                   ['A00050346', 'ACIT1515', 75],
        ...                   ['A00050346', 'ACIT1620', 49],
        ...                   ['A00035411', 'ACIT1420', 83],
        ...                   ['A00035411', 'ACIT1515', 81],
        ...                   ['A00035411', 'ACIT1620', 92],
        ...                   ['A00007991', 'ACIT1420', 66],
        ...                   ['A00007991', 'ACIT1515', 82],
        ...                   ['A00007991', 'ACIT1620', 82]]
        >>> get_course_averages(example_grades) #doctest: +NORMALIZE_WHITESPACE
        {'ACIT1420': 66.66666666666667, 'ACIT1515': 79.33333333333333,
        'ACIT1620': 74.33333333333333}

    """
    course_grades: dict = {}

    for grade_line in grades:
        course = grade_line[1]
        if course not in course_grades:
            course_grades[course] = []
        course_grades[course].append(grade_line[2])

    for course in course_grades:
        num_students = len(course_grades[course])
        total_grades = sum(course_grades[course])
        course_grades[course] = total_grades / num_students

    return course_grades


def get_student_grades(grades: list) -> dict:
    """
    Converts a list containing student ID, course, and grade to a dictionary
    index by student id that stores a diction of course ids holding the
    students grade.

    This is intended to facilitate fast lookup of student grades.


    Args:
        grades: this is a list of student ID, course, and grade received

    Returns:
        dict indexed by student id, which holds a nested dict indexed by course
        id and storing the grade received

    Examples:
        >>> example_grades = [['A00050346', 'ACIT1420', 51],
        ...                   ['A00050346', 'ACIT1515', 75],
        ...                   ['A00050346', 'ACIT1620', 49],
        ...                   ['A00035411', 'ACIT1420', 83],
        ...                   ['A00035411', 'ACIT1515', 81],
        ...                   ['A00035411', 'ACIT1620', 92],
        ...                   ['A00007991', 'ACIT1420', 66],
        ...                   ['A00007991', 'ACIT1515', 82],
        ...                   ['A00007991', 'ACIT1620', 82]]
        >>> get_student_grades(example_grades) #doctest: +NORMALIZE_WHITESPACE
        {'A00050346': {'ACIT1420': 51, 'ACIT1515': 75, 'ACIT1620': 49},
        'A00035411': {'ACIT1420': 83, 'ACIT1515': 81, 'ACIT1620': 92},
        'A00007991': {'ACIT1420': 66, 'ACIT1515': 82, 'ACIT1620': 82}}

    """
    student_grades: dict = {}

    for grade_line in grades:
        student_id, course, grade = grade_line[0], grade_line[1], grade_line[2]
        if student_id not in student_grades:
            student_grades[student_id] = {}
        student_grades[student_id][course] = grade

    return student_grades


if __name__ == '__main__':
    demo()
