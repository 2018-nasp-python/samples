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
    phrase1 = "This is a new phrase"
    word_list1 = phrase1.split()
    reversed_word_iterator = map(reverse_word, word_list1)
    reversed_word_list = list(reversed_word_iterator)
    pprint.pprint(reversed_word_list)


if __name__ == "__main__":
    main()
