def arg_func(p1, p2):
    print(p1, p2)


def args_func(*args):
    print(args)


def args_func_w_tuple(args):
    print(args)


def kwarg_func(a1='default_1', a2='default_2'):
    print(a1, a2)


def kwargs_func(**kwargs):
    print(kwargs)


def kwargs_func_w_dict(kwargs):
    print(kwargs)


def make_sandwich_args(*args):
    for ingredient in args:
        print(ingredient)


def make_sandwich_kwargs(**kwargs):
    for ingredient, amount in kwargs.items():
        print(ingredient + ": " + amount)
        

def main():
    # conventional function call
    arg_func(3, 4)

    # expanded list function call
    l1 = [3, 4]
    arg_func(*l1)

    # variable positional arguments function call
    args_func(3, 4)
    args_func(2, 3, 4)

    # using explicit tuple to perform variable positional arguments function
    # call
    t = (3, 4)
    args_func_w_tuple(t)

    t = (2, 3, 4)
    args_func_w_tuple(t)

    # Key word argument  function call
    kwarg_func(a1='v1', a2='v2')

    # expanded dictionary key word argument function call
    d1 = { 'a1': 'v2', 'a2': 'v2'}
    kwarg_func(**d1)

    # variable argument key word argument function call
    kwargs_func(a1='v1', a2='v2')
    kwargs_func(a1='v1', a2='v2', a3='v3')

    # using explicit dictionary to make variable argument key word argument
    # function call
    d1 = {'a1': 'v2', 'a2': 'v2'}
    d2 = {'a1': 'v2', 'a2': 'v2', 'a3': 'v3'}
    kwargs_func_w_dict(d1)
    kwargs_func_w_dict(d2)

    make_sandwich_args('bread', 'tomato', 'roast beef', 'mayo')
    make_sandwich_kwargs(bread='2', tomato='1', roast_beef='100', mayo='5')


if __name__ == '__main__':
    main()
