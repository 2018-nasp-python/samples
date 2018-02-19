#! /usr/bin/env python3
import pprint

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


def filter_w_function():
    powers_of_three = list(range(3,100,3))
    even_powers_of_three= list(filter(is_even, powers_of_three))
    pprint.pprint(even_powers_of_three)

def filter_w_lambda():
    powers_of_three = list(range(3,100,3))
    even_powers_of_three= list(filter(lambda num: num % 2 == 0, powers_of_three))
    pprint.pprint(even_powers_of_three)


if __name__ == "__main__":
    filter_w_function()
    filter_w_lambda()