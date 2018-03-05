#! /usr/bin/env python3
import sys
import argparse
import os

def show_args(argument_list):
    parser = argparse.ArgumentParser(description="Demonstration argument parser")
    parser.add_argument("command", help="command argument")
    parser.add_argument("-d", "--debug", help="debug switch", action="store_true")
    arguments = parser.parse_args(argument_list)
    print("command: {} debug: {}".format(arguments.command,arguments.debug))

if __name__ == '__main__':
    show_args(["some_command"])
    show_args(["-d", "other_command"])
    show_args(["other_command", "--debug"])
    show_args(["--debug", "last_command"])
    show_args(["-h"]) # this is considered and error and forces the script to exit
    
