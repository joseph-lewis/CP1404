password = input("Enter password: ")
while len(password) < 3:
    password = input("Enter password longer than 3 characters: ")
for char in password:
    print("*", end="")
