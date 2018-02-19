#!/usr/bin/env python3

def main(func_list):
    for func in func_list:
        func()

def print_hello():
    print("Hello")


def print_goodbye():
    print("Goodbye")


if __name__ == '__main__':
    list_of_functions = [print_hello, print_goodbye]
    main(list_of_functions)
