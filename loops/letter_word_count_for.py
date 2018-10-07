#! /usr/bin/env python3
"""Demonstrates nested for loops in calculating word and letter frequencies
"""

import pprint

def remove_punctuation(passage):
    """
    This function returns a string with all punctuation converted to spaces

    Args:
        passage: the source string

    Returns:
        string with no punctuation only spaces

    Note:
        There are better ways to do this (e.g. use regular expressions)
    """
    punctuation = ".", "'", '"', ";", ":", ",", "?"

    for i in punctuation:
        passage = passage.replace(i, " ")

    return passage

def word_letter_count(phrase):
    """Calculates word and letter frequencies for phrase
    
    Arguments:
        phrase (str):  phrase on which count word and letter frequencies will 
                       be calculated
    
    Returns:
        tuple: tuple containing two dictionaries - word count, and letter count
               indexed by words/ letters and storing the count for each
    """

    word_freq = {}
    letter_freq = {}

    words = remove_punctuation(phrase).lower().split()

    for word in words:

        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
        
        for letter in word:
            if letter in letter_freq:
                letter_freq[letter] += 1
            else:
                letter_freq[letter] = 1

    return word_freq, letter_freq

def main():
    """Uses word_letter_count to display the word and letter frequencies
    """

    phrase = "This is a sentence were both the words in the sentence and letters in the sentence will be counted. The counts of the letters and words will be stored in a dictionary"

    word_freq, letter_freq = word_letter_count(phrase)

    # Using pretty print results in a nice multi line sorted output
    pprint.pprint(word_freq)
    pprint.pprint(letter_freq)


if __name__ == '__main__':
    main()