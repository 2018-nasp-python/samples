#!/usr/bin/env python3
'''
Demonstration of using functions as arguments and invoking them.
'''
from typing import List, Callable


def print_hello():
    '''
    Simple demonstration function
    '''
    print("Hello")


def print_goodbye():
    '''
    Simple demonstration function
    '''
    print("Goodbye")


def main(func_list: List[Callable]):
    '''
    Simple function that accepts a list of functions and calls them in a loop

    Args:
        func_list (List[Callable]): [description]
    '''
    for func in func_list:
        func()


if __name__ == '__main__':
    list_of_functions = [print_hello, print_goodbye]
    main(list_of_functions)
