import inspect


def my_func(name):
    print("Hello {}".format(name))


def main():
    print(inspect.getsource(my_func))


if __name__ == '__main__':
    main()

