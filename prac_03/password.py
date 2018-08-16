def main():
    password = get_password()
    loop(password)


def loop(password):
    for char in password:
        print("*", end="")


def get_password():
    password = input("Enter password: ")
    while len(password) < 3:
        password = input("Enter password longer than 3 characters: ")
    return password


main()
