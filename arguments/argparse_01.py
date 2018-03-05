#! /usr/bin/env python3
import sys
import argparse

def show_args(argument_list):
    parser = argparse.ArgumentParser(description="Demonstration argument parser")
    parser.add_argument("command", help="command argument")
    parser.add_argument("-d", "--debug", help="debug switch", action="store_true")
    arguments = parser.parse_args()
    print(arguments.command)
    print(arguments.debug)
if __name__ == '__main__':
    show_args(sys.argv)