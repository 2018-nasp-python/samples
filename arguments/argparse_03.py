#! /usr/bin/env python3
import sys
import argparse
import os

def show_args(argument_list):
    parser = argparse.ArgumentParser(description="Demonstration argument parser")
    parser.add_argument("command", help="command argument", choices=['print', 'set', 'list'])
    parser.add_argument("-d", "--debug", help="debug switch", action="store_true")
    arguments = parser.parse_args(argument_list)
    print("command: {} debug: {}".format(arguments.command,arguments.debug))

if __name__ == '__main__':
    show_args(["print"])
    show_args(["-d", "list"])
    show_args(["other_command", "--debug"])
    
