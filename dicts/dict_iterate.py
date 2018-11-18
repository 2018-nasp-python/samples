#! /usr/bin/env python3
'''
Demonstration of looping over and sorting dictionaries
'''
from typing import List, Tuple


def get_value(key_value: Tuple[str, int]) -> int:
    '''
    Returns the value portion of a key / value tuple

    Args:
        key_value (Tuple[str, int]): the key / value tuple to from which to
                                     retrieve the value

    Returns:
        int: the value of the key / value tuple
    '''

    return key_value[1]


def get_value_sum(key_value: Tuple[str, List[int]]) -> int:
    '''
    Returns the sum of the numbers stored in the value portion of a key / value
    tuple where the value is a list of integers.

    Args:
        key_value (Tuple[str, List[int]]): the key / value tuple to from which
                                           to retrieve and sum the list of
                                           numbers

    Returns:
        int: sum of all the numbers in value portion of tuple
    '''

    return sum(key_value[1])


def main():

    # Dictionary with string key and integer value
    d01 = {"key04": 2,
           "key05": 1,
           "key01": 5,
           "key03": 3,
           "key02": 4}

    # Dictionary with string key and list of integers for values
    d02 = {"key04": [2, 3, 40, 5],
           "key05": [1, 2, 30, 4, 5],
           "key01": [5],
           "key03": [3, 4, 50],
           "key02": [4, 5]}

    print('Printing d01 Keys in insertion order')
    for key in d01.keys():
        print("Key: {}".format(key))

    print('\nPrinting d01 values in insertion order')
    for value in d01.values():
        print("Value: {}".format(value))

    print('\nPrinting d01 key / values in insertion order')
    for key, value in d01.items():
        print("Key: {}\tValue: {}".format(key, value))

    print('\nPrinting d01 key / values in insertion order')
    for tup in d01.items():
        print("Key: {}\tValue: {}".format(tup[0], tup[1]))

    print('\nPrinting d01 key / values sorted by key')
    key_sorted_d01 = sorted(d01.items())
    for tup in key_sorted_d01:
        print("Key: {}\tValue: {}".format(tup[0], tup[1]))

    print('\nPrinting d01 key / values sorted by value')
    # Note the passing of the get_value function by name as the key argument to
    # the sorted function
    #
    # This is used to determine that value for each tuple that will be used for
    # sorting
    #
    # This function is called for each item in the dictionary in the form
    # get_value(item) where item is a tuple of the form (name, value)
    value_sorted_d01 = sorted(d01.items(), key=get_value)
    for tup in value_sorted_d01:
        print("Key: {}\tValue: {}".format(tup[0], tup[1]))

    print('\nPrinting d02 key / values sorted by value')
    # Note the passing of the get_sum function by name as the key argument to
    # the sorted function
    #
    # This is used to determine that value for each tuple that will be used for
    # sorting
    #
    # This function is called for each item in the dictionary in the form
    # get_value(item) where item is a tuple of the form (name, value)
    # In this case each value is actually list of integers
    value_sorted_d02 = sorted(d02.items(), key=get_value_sum)
    for key, value in value_sorted_d02:
        print("Key: {}\tValue: {}".format(key, sum(value)))

    print('\nPrinting d02 key / values sorted by value, in reverse')
    # Note the passing of the get_sum function by name as the key argument to
    # the sorted function. Additionally the reverse argument is set to true.
    # This will invert the sort order
    #
    # The get_sum function is used to determine that value for each tuple that
    # will be used for sorting
    #
    # This function is called for each item in the dictionary in the form
    # get_value(item) where item is a tuple of the form (name, value)
    # In this case each value is actually list of integers
    value_sorted_d02 = sorted(d02.items(), key=get_value_sum, reverse=True)
    for key, value in value_sorted_d02:
        print("Key: {}\tValue: {}".format(key, sum(value)))

if __name__ == '__main__':
    main()
