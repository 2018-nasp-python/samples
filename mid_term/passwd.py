#! /usr/bin/env python3
"""
Module that incorporates a main function to get user input and a validate
function to test user passwords for proper formatting.
"""


def validate(password: str) -> str:
    """Validate the supplied password, return valid or the rules violated by
        the password.

    Validate the supplied password according to the following rules:

        Password must contain a special character from the following:
            ~`!@#$%^&*+=_-:;?<>,.

        Password must contain a number.

        Password must be 8 characters long.

        Password must contain an uppercase consonant. Specifically 1 of:
            BCDFGHJKLMNPQRSTVWX

        Password must contain a lowercase vowel. Specifically 1 of:
            aeiouy

    Arguments:

        password (str): password to be tested against password composition
                        rules

    Returns:

        (str): Message containing "Valid" if the password meets all of the
               rules or a combined error message containing all of the rules
               that were broken by the password.

               Missing special character:
                   "Password must contain a special character"
               Missing a number number:
                   "Password must contain a number"
               Password is too short:
                   "Password must be 8 characters long"
               Password doesn't contain an uppercase consonant:
                   "Password must contain an uppercase consonant"
               Password doesn't contain a lowercase vowel:
                   "Password must contain a lowercase vowel"

    """

    MIN_LENGTH = 8
    SPECIAL_CHARS = "~`!@#$%^&*+=_-:;?<>,."
    NUMBERS = '0123456789'
    UPPERCASE_CONSONANT = 'BCDFGHJKLMNPQRSTVWXZ'
    LOWERCASE_VOWEL = 'aeiouy'

    special_error = "Password must contain a special character\n"
    numbers_error = "Password must contain a number\n"
    length_error = "Password must be {} characters long\n".format(MIN_LENGTH)
    uppercase_error = "Password must contain an uppercase consonant\n"
    lowercase_error = "Password must contain a lowercase vowel\n"

    if len(password) >= MIN_LENGTH:
        length_error = ""

    for character in password:
        if character in SPECIAL_CHARS:
            special_error = ""
        elif character in NUMBERS:
            numbers_error = ""
        elif character in UPPERCASE_CONSONANT:
            uppercase_error = ""
        elif character in LOWERCASE_VOWEL:
            lowercase_error = ""

    error_message = (special_error + numbers_error + length_error +
                     uppercase_error + lowercase_error)

    if len(error_message) == 0:
        return "Valid"
    else:
        return error_message


def main():
    """Prompt a the user for a password and print the password verification result
    """

    password = input("Input password: ")
    print(validate(password))


if __name__ == "__main__":
    main()
