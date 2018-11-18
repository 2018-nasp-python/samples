#! /usr/bin/env python3
"""Simple script that echoes all of the arguments passed to the script
"""
import sys

for arg_count, arg in enumerate(sys.argv):
    print("sys.argv[{}] Value: {}".format(arg_count, arg))
    arg_count += 1
