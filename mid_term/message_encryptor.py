#! /usr/bin/env python3

import pprint
import random
import string
from typing import Dict


def generate_cipher() -> Dict[str, str]:
    '''
    Generates a dictionary that maps each ASCII letter (upper and lower case)i
    to its scambled equivalent

    Notes:
        1. list(string.ascii_letters) - generates a list of a the ASCII letter
           characters.
        1. random.shuffle(list1) - will shuffle a list1 in place

    Returns:
        Dict[str, str]: cipher dictionary with one item per ASCII letter
    '''
    cipher = {}

    letters = list(string.ascii_letters)
    scrambled_letters = letters.copy()
    random.shuffle(scrambled_letters)

    for letter_pos in range(len(letters)):
        cipher[letters[letter_pos]] = scrambled_letters[letter_pos]

    # alternative: cipher = dict(zip(letters,scrambled_letters))

    return cipher


def generate_rev_cypher(cipher: Dict[str, str]) -> Dict[str, str]:
    '''
    Returns and reverse cipher to map from encrypted cipher text back to plain
    text. It creates the reverse cipher by looping over the passed cipher and
    creating a new dictionary that maps uses the value of the cipher parameter
    as the reverse cipher key and the key of the original as the reverse cipher
    value.

    Args:
        cipher (Dict[str,str]): encryption cipher to be reversed

    Returns:
        Dict[str,str]: decryption cipher that preforms the reverse mapping of
                       the input cipher
    '''
    rev_cipher = {}

    for orig, trans in cipher.items():
        rev_cipher[trans] = orig

    return rev_cipher


def encode_message(cipher, message):
    '''
    This function converts each letter in the message to the one specified in
    the cipher dictionary.  It then returns the transformed message. It leaves
    non-letter characters unchanged.

    Args:
        cipher (Dict[str,str]): a dictionary that maps an input character to
                                its transformed equivalent

        message (str): A string to be transformed using the cipher

    Returns:
        str: the transformed string
    '''
    transformed_message = ""

    for letter in message:
        if letter in string.ascii_letters:
            letter = cipher[letter]
        transformed_message += letter

    return transformed_message


def main():
    '''
    Creates an encryption cipher dictionary using generate_cipher()
    Creates an decryption cipher dictionary using generate_rev_cipher()

    For each of the individual messages in messages:
        - encrypt the message using encode_message()
        - print the encrypted message
        - decrypt the message using encode_message()
        - print the decrypted original message.
    '''
    messages = ["Tests aren't easy",
                "Documentation makes programming easier",
                "This is the last message"]

    encryption_cipher = generate_cipher()
    decryption_cipher = generate_rev_cypher(encryption_cipher)

    print("\nCipher:")
    pprint.pprint(encryption_cipher)

    print("\nReverse Cipher:")
    pprint.pprint(decryption_cipher)
    print()

    for message in messages:
        scrambled_message = encode_message(encryption_cipher, message)
        print("Scrambled Message: {}".format(scrambled_message))
        orig_message = encode_message(decryption_cipher, scrambled_message)
        print("Original Message: {}".format(orig_message))


if __name__ == '__main__':
    main()
