"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""


def main():
    with open('temps_input.txt') as tempf:
        tempsf = tempf.readlines()
        with open('temps_output.txt', 'w') as tempc:
            for tempf in tempsf:
                tempc.write(f"{f2c(float(tempf))}\n")


def f2c(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


if __name__ == '__main__':
    main()
