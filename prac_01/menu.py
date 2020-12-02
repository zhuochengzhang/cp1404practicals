name = input("Get Name: ")
MENU = """H Hello
G Goodbye
Q quit"""
print(MENU)
choice = input("Get Choice: ").upper()
while choice != "Q":
    if choice == "H":
        print("Hello {}".format(name))
    elif choice == "G":
        print("Goodbye {}".format(name))
    else:
        print("Invalid Choice")
    choice = input("Get Choice: ").upper()
