#! /usr/bin/env python3
"""Demonstrates nested while loops in calculating word and letter frequencies
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
    punctuation_index = 0 
    while punctuation_index < len(punctuation):
        passage = passage.replace(punctuation[punctuation_index], " ")
        punctuation_index += 1

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
    word_index = 0 
    
    while word_index < len(words):

        if words[word_index] in word_freq:
            word_freq[words[word_index]] += 1
        else:
            word_freq[words[word_index]] = 1
        
        word = words[word_index]
        letter_index = 0 

        while letter_index < len(word):
            if word[letter_index] in letter_freq:
                letter_freq[word[letter_index]] += 1
            else:
                letter_freq[word[letter_index]] = 1
            
            letter_index += 1
        
        word_index += 1

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