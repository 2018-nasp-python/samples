#! /usr/bin/env python3
import copy


def print_id(var, depth=0):
    indent = " " * depth
    depth += 1
    if type(var) is list:
        print("{}{}".format(indent, id(var)))
        print("{}[ ".format(indent))
        for sub_var in var:
            print_id(sub_var, depth)
        print("{}] ".format(indent))
    else:
        indent = " " * depth
        print("{}{}".format(indent, id(var)))


orig = ['e0', 'e1', 'e2']
orig_assign = orig
orig_copy = orig.copy() 
orig_deep_copy = copy.deepcopy(orig)

print('orig')
print_id(orig)
print('\norig_assign')
print_id(orig_assign)
print('\norig_copy')
print_id(orig_copy)
print('\norig_deep_copy')
print_id(orig_deep_copy)

nested_orig = [['e0s0', 'e0s1'], ['e1s0', 'e1s1'], ['e2s0', 'e2s1']]
nested_orig_assign = nested_orig
nested_orig_copy = nested_orig.copy()
nested_orig_deep_copy = copy.deepcopy(nested_orig)

print('\nnested_orig')
print_id(nested_orig)
print('\nnested_orig_assign')
print_id(nested_orig_assign)
print('\nnested_orig_copy')
print_id(nested_orig_copy)
print('\nnested_orig_deep_copy')
print_id(nested_orig_deep_copy)
