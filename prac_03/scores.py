"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

from random import randrange


def main():
    number = int(input("Enter : number of scores"))
    for _ in range(number):
        score = randrange(100)
        result = score_result(score)
        print(f"{score} is {result}")


def score_result(score):
    if score < 0:
        return "Invalid score"
    else:
        if score > 100:
            return "Invalid score"
        if score > 50:
            return "Passable"
        if score > 90:
            return "Excellent"
    if score < 50:
        return "Bad"


if __name__ == '__main__':
    main()
