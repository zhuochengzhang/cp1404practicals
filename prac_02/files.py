def input_name():
    f = open("files.txt", "w")
    name = input("Input Name: ")
    f.write(name)


def output_name():
    f = open("files.txt")
    name = f.read()
    print("Your name is {}".format(name))


def input_numbers():
    f = open("numbers.txt", "w")
    f.write("17" + "\n")
    f.write("42" + "\n")
    f.write("200" + "\n")


def output_numbers():
    f = open("numbers.txt")
    lines = f.readlines()
    for line in lines:
        print(line.replace("\n", ""))


input_name()
output_name()

input_numbers()
output_numbers()
