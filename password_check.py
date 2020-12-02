def main():
    password = input("Input the password")
    if check_length(password):
        print("*" * len(password))
    else:
        print("password check not passed")


def check_length(password):
    min_length = 6
    return len(password) >= min_length


if __name__ == '__main__':
    main()
