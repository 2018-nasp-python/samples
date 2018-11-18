#! /usr/bin/env python3
import os


def main():
    # Get current directory of script
    script_dir = os.path.dirname(__file__)

    # Use a file path relative to the executing file so that we always know
    # where the input is is coming form
    man_page_path = os.path.join(script_dir, 'example_data', 'uname.txt')

    with open(man_page_path) as man_page_file:
        whole_file_as_string = man_page_file.read()
    print(whole_file_as_string)

    with open(man_page_path) as man_page_file:
        whole_file_line_list = man_page_file.readlines()
    print(whole_file_line_list)

    with open(man_page_path) as man_page_file:
        first_line = man_page_file.readline()
    print(first_line)

    with open(man_page_path) as man_page_file:
        for line in man_page_file:
            if line == "AUTHOR\n":
                author = man_page_file.readline().strip("Written by ").rstrip(".\n")

    print("\n\n The author was {}".format(author))


if __name__ == "__main__":
    main()
