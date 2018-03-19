#! /usr/bin/env python3
import traceback

class SimpleIntCalcWithCM:

    def __enter__(self):
        print("\nSimple Calc Setup started")
        return self

    def add(self, numerator, denominator):
        answer = int(int(numerator) / int(denominator))
        print("{} + {} = {}".format(numerator, denominator, answer)) 

    def subtract(self, numerator, denominator):
        answer = int(int(numerator) / int(denominator))
        print("{} - {} = {}".format(numerator, denominator, answer)) 

    def multiply(self, numerator, denominator):
        answer = int(int(numerator) / int(denominator))
        print("{} + {} = {}".format(numerator, denominator, answer)) 

    def divide(self, numerator, denominator):
        answer = int(int(numerator) / int(denominator))
        print("{} / {} = {}".format(numerator, denominator, answer)) 

    def __exit__(self, exception_type, exception_value, exception_traceback):

        if exception_type != None:
            print("\nBad stuff happend")
            print("Here is the kind of error: {}".format (exception_type))
            print("Here is the specific return value of the error: {}".format (exception_value))
            traceback.print_tb(exception_traceback)

        print("Simple Calc Cleanup done\n")

        return True


if __name__ == "__main__":

    values = [(10, 2), (4,3), (5,0), ("x", 8)]

    print("Using calculator using 'with' statement") 
    for value_pair in values:
        with SimpleIntCalcWithCM() as calculator:
            calculator.divide(value_pair[0], value_pair[1])

    print("\nUsing calculator without 'with' statement") 
    for value_pair in values:
        calculator = SimpleIntCalcWithCM()
        calculator.divide(value_pair[0], value_pair[1])
