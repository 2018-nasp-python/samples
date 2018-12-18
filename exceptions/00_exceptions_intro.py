#! /usr/bin/env python3


def raise_exc(exc_option):

    if exc_option == 'SyntaxError':
        raise SyntaxError("Intentionally raised SyntaxError Exception")
    elif exc_option == 'NameError':
        raise NameError("Intentionally raised NameError Exception")
    elif exc_option == 'KeyError':
        raise KeyError("Intentionally raised KeyError Exception")
    elif exc_option == 'IndexError':
        raise IndexError("Intentionally raised IndexError Exception")
    elif exc_option == 'FileNotFoundError':
        raise FileNotFoundError("Intentionally raised FileNotFoundError Exception")
    elif exc_option == 'TimeoutError':
        raise TimeoutError("Intentionally raised TimeoutError Exception")
    elif exc_option == 'ValueError':
        raise TimeoutError("Intentionally raised ValueError Exception")
    else:
        return "Success"


def exc_processing():

    exc_types = {
                    0: 'Success',
                    1: 'SyntaxError',
                    2: 'NameError',
                    3: 'KeyError',
                    4: 'IndexError',
                    5: 'FileNotFoundError',
                    6: 'TimeoutError',
                    7: 'ValueError'
    }

    print("""Exception Options
    0: Success - no exception
    1: SyntaxError - normally raised during import of module with syntax errors
    2: NameError - normally raised when accessing an undeclared variable
    3: KeyError - normally raised when accessing a dict using an invalid key
    4: IndexError - normally raised when accessing a list using an invalid index 
    5: FileNotFoundError - normally raised when opening non-existent file
    6: TimeoutError - normally raised when an os operation takes too long
    7: ValueError - normally raised when an argument is set to an improper value
    """)

    exc_option = int(input("Enter exception option: "))

    try:
        status = raise_exc(exc_types[exc_option])
    except NameError as error:
        print("NameError Details: {}".format(error))
    except KeyError as error:
        print("KeyError Details: {}".format(error))
    except IndexError as error:
        print("IndexError Details: {}".format(error))
    except FileNotFoundError as error:
        print("FileNotFoundError Details: {}".format(error))
    except TimeoutError as error:
        print("TimeoutError Details: {}".format(error))
    else:
        print('The exc_option function returned: {}'.format(status))
        return status
    finally:
        print('Finished exc_processing')


if __name__ == '__main__':
    exc_processing()
