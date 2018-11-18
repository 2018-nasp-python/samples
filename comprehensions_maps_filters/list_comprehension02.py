#! /usr/bin/env python3
import pprint

def percentage(total, num):
    percent = (num / total * 100)
    return percent


assignment_total = 45
student_raw_scores = [42, 36, 22, 29, 44, 45, 30]

student_percent_scores = [percentage(assignment_total, grade) for grade in student_raw_scores]
pprint.pprint(student_percent_scores)

s_p_s_2 = [((grade / assignment_total) * 100) for grade in student_raw_scores]
pprint.pprint(s_p_s_2)
