#! /usr/bin/env python3

import pprint
from word_utils import reverse_word

def main():
    phrase1 = "This is a new phrase"
    word_list1 = phrase1.split()
    reversed_word_iterator  = map(reverse_word, word_list1)
    reversed_word_list = list(reversed_word_iterator)
    pprint.pprint(reversed_word_list)

if __name__ == "__main__":
    main()