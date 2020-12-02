"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

finished = False
result = 0
while not finished:
    try:
        number = input("Input Number: ")
        number = int(number)
        finished = True
        result = number
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)
