#! /usr/bin/env python3
"""Writing Text to a File
"""
import os


def main():
    # Get current directory of script
    script_dir = os.path.dirname(__file__)

    # Use a file path relative to the executing file so that we always know
    # where the output is going
    over_write_path = os.path.join(script_dir, 'example_data', 'over_write_file.txt')
    append_path = os.path.join(script_dir, 'example_data', 'append_file.txt')

    # see https://docs.python.org/3/library/functions.html#open for details of
    # opening modes
    over_write_file = open(over_write_path, 'w')
    append_file = open(append_path, 'a')

    text = ""
    print("Write to files: Part 1")
    while True:
        text = input("Enter input or 'EOF' to quit: ")
        if text == "EOF":
            break

        # Uses format string method for ouput see:
        # https://docs.python.org/3/tutorial/inputoutput.html#fancier-output-formatting
        over_write_file.write("{}\n".format(text))
        append_file.write("{}\n".format(text))

    # Close files,  flushing them to disk
    over_write_file.close()
    append_file.close()

    over_write_file = open(over_write_path, 'w')
    append_file = open(append_path, 'a')
    text = ""
    print("Write to files: Part 2 - no newline")
    while True:
        text = input("Enter input or 'EOF' to quit: ")
        if text == "EOF":
            break
        over_write_file.write(text)
        append_file.write(text)

    # Close files,  flushing them to disk
    over_write_file.close()
    append_file.close()


if __name__ == "__main__":
    main()