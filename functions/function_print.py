#! /usr/bin/env python3
'''
Simple Demonstration that functions are variables / objects too
'''
# from the documentation (https://docs.python.org/3/library/inspect.html):
#  The inspect module provides several useful functions to help get
#  information about live objects such as modules, classes, methods, functions,
#  tracebacks, frame objects, and code objects
import inspect

# from the documentation (https://docs.python.org/3/library/dis.html):
#   The dis module supports the analysis of CPython bytecode by disassembling
#   it.
import dis


def my_func(name):
    print("Hello {}".format(name))


def print_source(function):
    '''
    Write function source to standard out
    
    Args:
        function (Function): function whose source is to be printed
    '''

    function_source = inspect.getsource(function)
    print(function_source)

def print_bytecode(function):
    '''
    Write function bytecode to standard out
    
    Args:
        function (Function): function whose bytecode is to be printed
    '''
    dis.dis(function)

def main():
    print_source(my_func)
    print_bytecode(my_func)


if __name__ == '__main__':
    main()