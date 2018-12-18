import sys


def quit():
    sys.exit()


def frog():
    print('ribbit ribbit ribbit')
    return


def get_int(prompt='Enter an integer'):

    while True:
        # Activity 6
        n = input('\n%s: ' % prompt)
        return int(n)


def get_range():
    low = get_int('Enter a lower bound for the range')
    high = get_int('Enter an upper bound for the range')

    while True:
        # Activity 7
        prompt = 'Enter a value that is in range {} - {}'.format(low, high)
        value = get_int(prompt)
        check_range(low, high, value)
        break
        
   return (value, low, high)


def check_range(low, high, value):
    # Activity 7

def get_path():
    pass


def find_file(filename, pathname):
    pass
