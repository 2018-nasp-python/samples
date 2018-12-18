#! /usr/bin/env python3


def main():
    try:
        with open('non_existent', 'r') as source:
            data = source.readlines()
            print(data)

    except FileNotFoundError as error:
        print(error.strerror)


if __name__ == '__main__':
    main()
