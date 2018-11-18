#! /usr/bin/env python3
"""Writing Text to a File using with statement
"""
import os


def main():
    # Get current directory of script
    script_dir = os.path.dirname(__file__)

    # Use a file path relative to the executing file so that we always know
    # where the output is going
    over_write_path = os.path.join(script_dir,
                                   'example_data', 'over_write_file.txt')

    append_path = os.path.join(script_dir, 'example_data', 'append_file.txt')

    # see https://docs.python.org/3/library/functions.html#open for details of
    # opening modes
    with open(over_write_path, 'w') as over_write_file, open(append_path, 'a') as append_file:

        text = ""
        print("Write to files: Part 1")
        while True:
            text = input("Enter input or 'EOF' to quit: ")
            if text == "EOF":
                break

            # Uses format string method for printing see:
            # https://docs.python.org/3/tutorial/inputoutput.html#fancier-output-formatting
            over_write_file.write("{}\n".format(text))
            append_file.write("{}\n".format(text))


if __name__ == "__main__":
    main()
