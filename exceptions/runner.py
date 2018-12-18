import os
import sys
import commands


def read_menu_from_file(filename):

    dictionary = {}
    
    #Activity 3
    with open(filename, 'r') as f:

        for i,line in enumerate(f):
            # Activity 4
            [key, value] = line.split()
            dictionary[int(key)] = value


    return dictionary


def get_choice(menu):

    while True:
        for cmd_num,cmd_name in menu.items():
            print("%i - %s" % (cmd_num, cmd_name))
        
        # Activity 8
        num = int(input('\nEnter command: '))
        return num

def main(argv):

    # Activity 2 
    menu = read_menu_from_file(argv[1])

    print('\nWelcome to %s\n' % os.path.basename(argv[0]))


    while True:
        choice = get_choice(menu)

        # Activity 5
        run_cmd = getattr(commands, menu[choice])
        result = run_cmd()
        print('Function %s() returned: %s\n' % (menu[choice], str(result)))

if __name__ == '__main__':
    main(sys.argv)
