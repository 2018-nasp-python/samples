#! /usr/bin/env python3
import os


def main():

    # Get current directory of script
    script_dir = os.path.dirname(__file__)

    # Use a file path relative to the executing file so that we always know
    # where the input is is coming from
    man_page_path = os.path.join(script_dir, 'example_data', 'uname.txt')

    man_page_file = open(man_page_path)
    whole_file_as_string = man_page_file.read()
    man_page_file.close()
    print(whole_file_as_string)

    man_page_file = open(man_page_path)
    whole_file_line_list = man_page_file.readlines()
    print(whole_file_line_list)
    man_page_file.close()

    man_page_file = open(man_page_path)
    first_line = man_page_file.readline()
    print(first_line)
    man_page_file.close()

    man_page_file = open(man_page_path)

    for line in man_page_file:
        if line == "AUTHOR\n":
                author = man_page_file.readline().strip("Written by ").rstrip(".\n")
    if author:
        print(author)

    man_page_file.close()


if __name__ == "__main__":
    main()
