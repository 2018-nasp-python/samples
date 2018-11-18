#! /usr/bin/env python3


def make_list(p1, p2, p3):
    new_list = [p1, p2, p3]
    return new_list


def list_pop(list_param):
    removed_elem = list_param.pop()
    return removed_elem


l1 = make_list(1, 2, 3)
l2 = l1

print(l1)
print(l2)

removed_item = list_pop(l2)

print(removed_item)
print(l1)
print(l2)