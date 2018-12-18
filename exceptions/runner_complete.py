import os
import sys
import commands


def read_menu_from_file(filename):

    dictionary = {}
    try:
        f = open(filename, 'r')
    except FileNotFoundError as err:
        print(err)
        exit()

    for i,line in enumerate(f):
        try:
            [key, value] = line.split()
        except ValueError:
            print('Line %i in %s has %i tokens. Expecting 2.' % (i, filename, len(line.split())))
            exit()
        try:
            dictionary[int(key)] = value
        except ValueError:
            print('Command number not an integer: %s' % (line))
            exit()

    f.close()

    return dictionary


def get_choice(menu):

    while True:
        for cmd_num,cmd_name in menu.items():
            print("%i - %s" % (cmd_num, cmd_name))
        try:
            num = int(input('\nEnter command: '))
            valid_nums = [key for key in menu.keys()]
            if num not in valid_nums:
                raise ValueError
            else:
                return num
        except ValueError:
            choices = " ".join([str(key) for key in menu.keys()])
            print('\nInvalid selection. Choose one of: %s\n' % choices)


def main(argv):

    try:
        menu = read_menu_from_file(argv[1])
    except IndexError:
        print('Usage: runner.py <filename>')
        exit()

    print('\nWelcome to %s\n' % os.path.basename(argv[0]))


    while True:
        choice = get_choice(menu)

        try:
            run_cmd = getattr(commands, menu[choice])
            result = run_cmd()
            print('Function %s() returned: %s\n' % (menu[choice], str(result)))
        except AttributeError:
            print('Error: command %s not implemented.' % menu[choice])
            exit()


if __name__ == '__main__':
    main(sys.argv)
