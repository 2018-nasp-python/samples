import random
import json
from typing import List
from typing import Tuple


def generate_student_ids(num_students: int) -> List[str]:
    """
    Generates a list of of random BCIT student IDs

    Args:
        num_students: the number of student IDs to generate

    Returns:
        a list of random student ID's

    Examples:
        >>> generate_student_ids(5) #doctest: +ELLIPSIS
        ['A0...', 'A00...', 'A00...', 'A00...', 'A00...']

    """
    max_sid_suffix = 999999
    random_suffixes = random.sample(range(1, max_sid_suffix + 1), num_students)
    student_ids = ['A00{:=06}'.format(suffix) for suffix in random_suffixes]

    return student_ids


def generate_course_grades(student_ids: List[str], courses: Tuple[str], file_name: str):
    """
    Generates a json grades file with a student grade per course

    Args:
        student_ids: a list of student ID's
        courses: a list of course codes
        file_name:  the file to save the generated data to

    Examples:
        >>> s_ids = ['A00123456', 'A00987654']
        >>> course_codes = ('ACIT_0101', 'ACIT_0201')
        >>> generate_course_grades(s_ids, course_codes, "sample_grades.json")
        >>> with open('sample_grades.json') as grades_file:
        ...     sample_grades = json.load(grades_file)
        >>> sample_grades #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
        [['A00123456', 'ACIT_0101', ...], ['A00123456', 'ACIT_0201', ...],
        ['A00987654', 'ACIT_0101', ...], ['A00987654', 'ACIT_0201', ...]]

    """
    max_grade = 100
    min_grade = 45
    grades = []
    for student_id in student_ids:
        for course in courses:
            grades.append([student_id, course, random.randint(min_grade, max_grade + 1)])

    with open(file_name, "w") as grades_file:
        json.dump(grades, grades_file)


def main():
    """
    Generates grades.json file for use in docstring_doctest_demo_with_variables.py
    """
    courses = ("ACIT1420", "ACIT1515", "ACIT1620", "ACIT1630", "COMM1116", "MATH1310", "ORGB1100")
    sids = generate_student_ids(24)
    generate_course_grades(sids, courses, "grades.json")


if __name__ == '__main__':
    main()
