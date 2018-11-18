#! /usr/bin/env python3
"""
Module that incorporates a main function to get user input and a validate
function to test postal codes for proper formatting.
"""


def validate(postal_code: str) -> str:
    """Validate the supplied postal code, return "Valid" or the rules it broke

    Validate that the supplied postal code follows the following format:

        CNCNCN
    or 

        CNC NCN

    Where 
        C: means an upper or lowercase character
        N: means a number

    Arguments:
        postal_code (str):  postal code to be tested against composition rules
    
    Returns:
        str: Message containing "Valid" if the postal code meets all of the
             rules or a combined error message containing all of the rules that
             were broken and the character in the postal code that broke them.
         
    """

    PC_LENGTH = 6
    error_message = []

    pc_compressed = postal_code.replace(" ", "")

    if len(pc_compressed) != PC_LENGTH:
        error_message.append("A Postal Code must be 6 characters long")

    for pos, character in enumerate(pc_compressed):
        if pos % 2 == 0 and not character.isalpha():
            error_message.append('Postal Code character {} must be a letter not "{}"'.format(pos + 1, character))
        elif pos % 2 != 0 and not character.isnumeric():
            error_message.append('Postal Code character {} must be a number not "{}"'.format(pos + 1, character))
  

    if len(error_message) == 0:
        return "Valid"
    else:
        output = ""
        for message in error_message:
            output += message + "\n"
        return output
        

def main():
    """
    Prompt a the user for a password and print the password verification result
    """

    postal_code = input("Input postal code: ")
    print(validate(postal_code))

if __name__ == "__main__":
    main()