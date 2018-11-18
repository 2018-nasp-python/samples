#! /usr/bin/env python3
import pprint

def reverse_word(word):
    word_len = len(word)
    char_pos = word_len - 1
    reversed_word = ""
    while char_pos >= 0:
        reversed_word = reversed_word + word[char_pos].lower()
        char_pos = char_pos - 1

    return reversed_word


def main():
    phrase = "This is truly original here"
    word_list = phrase.split()

    reversed_word_list = [reverse_word(word) for word in word_list]

    pprint.pprint(reversed_word_list)   


if __name__ == "__main__":
    main()