#! /usr/bin/env python3
import os
# Get current directory of script
script_dir = os.path.dirname(__file__)

# Use a file path relative to the executing file so that we always know where 
# the input is is coming form 
man_page_path = os.path.join(script_dir, 'example_data', 'uname.txt')
non_existent_path = os.path.join(script_dir, 'example_data', 'non_existant.txt')

with open(man_page_path) as man_page_file:
    whole_file_as_string = man_page_file.read()
print(whole_file_as_string)

with open(man_page_path) as man_page_file:
    whole_file_line_list = non_existent_file.readlines()
print(whole_file_line_list)

with open(man_page_path) as man_page_file:
    first_line = non_existent_file.readline()
print(first_line)

with open(man_page_path) as man_page_file:
    for line in man_page_file:
        if line == "AUTHOR\n":
            author = man_page_file.readline().strip("Written by ").rstrip(".\n")
print("\n\n The authour was {}".format(author))