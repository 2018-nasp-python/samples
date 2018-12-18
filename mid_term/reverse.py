#! /usr/bin/env python3


def reverse(phrase):
    num_letters = len(phrase)
    letter_count = 1
    reversed_phrase = ""

    while letter_count < num_letters:
        reversed_phrase += phrase[num_letters - letter_count]
        letter_count += 1

    return reversed_phrase


def main():

    phrases = []
    phrases.append("Exams are not the most authentic of assessments")
    phrases.append("Loops need to end")
    phrases.append("Exams are not the most authentic of assessments")

    for phrase in phrases:
        print(reverse(phrase))


if __name__ == '__main__':
    main()
