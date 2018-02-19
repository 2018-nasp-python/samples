def reverse_word(word):
    word_len = len(word)
    char_pos = word_len - 1
    reversed_word = ""
    while char_pos >= 0:
        reversed_word = reversed_word + word[char_pos].lower()
        char_pos = char_pos - 1

    return reversed_word

