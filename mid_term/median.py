#! /usr/bin/env python3
import statistics

def main():

    num_strings = input("Enter numbers to find the median: ").split()
    num_floats = [float(num) for num in num_strings]
    median = statistics.median(num_floats)
    print(median)

if __name__ == "__main__":
    main()
