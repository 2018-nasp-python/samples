def variable_args(*args):
    """


    The asterisk (*) is the important element here, as the word args is the
    established conventional idiom, though it is not enforced by the language

    Args:
        *args: an arbitrary sized list of values

    Returns:
        None

    """
    for arg in args:
        print(str(arg))


def variable_kwargs(**kwargs):
    """

    The two asterisks (**) are the important element here, as the word kwargs is
    conventionally used, though not enforced by the language.

    Args:
        **kwargs:
            an arbitrary sized dictionary of name: value pairs

    Returns:
        None

    """
    for key, value in sorted(kwargs.items()):
        print('Key: {:20} Value: {:20}'.format(key, value))


def args_demo():

    variable_args("hello", "my", "friends")
    variable_args(0, 1, 1, 2, 3, 5, 8, 13)
    variable_kwargs(student_id='A00123456', acit_1620="76.45")
    variable_kwargs(student_id='A00123456', acit_1620="76.45")


if __name__ == '__main__':
    args_demo()



