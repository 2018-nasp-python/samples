#! /usr/bin/env python3
import pprint
from word_utils import reverse_word

phrase = "This is truly original here"
word_list = phrase.split()

reversed_word_list = [reverse_word(word) for word in word_list]

pprint.pprint(reversed_word_list)   

