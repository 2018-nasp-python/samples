#! /usr/bin/env python3
import sys

def show_args(argument_list):
    arg_count = 0
    for arg in sys.argv:
        print("Argument: {} Value: {}".format(arg_count,arg))
        arg_count += 1

if __name__ == '__main__':
    show_args(sys.argv)