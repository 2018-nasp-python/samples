#! /usr/bin/env python3
"""Simple script that echoes all of the arguments passed to the script
"""

import sys

arg_count = 0
for arg in sys.argv:
    print("Argument: {} Value: {}".format(arg_count,arg))
    arg_count += 1

