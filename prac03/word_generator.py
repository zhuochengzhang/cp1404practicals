"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"


def main():
    valid = False
    while not valid:
        word_format = input("Input the word format: ")
        valid = is_valid_format(word_format)
    word = ""
    for kind in word_format:
        if kind == "c":
            word += random.choice(CONSONANTS)
        else:
            word += random.choice(VOWELS)

    print(word)


def is_valid_format(word_format):
    for ch in word_format:
        if ch != 'c' and ch != 'v':
            return False
    return True


if __name__ == '__main__':
    main()
