LOWER = 33
UPPER = 127

def main():
    char = input("Enter character: ")
    print("The ASCII code for {} is {}".format(char, ord(char)))
    number = int(input("Enter a number between 33 and 127: "))
    new_number = get_number(number)
    print("The character for {} is {}".format(new_number, (chr(int(new_number)))))
    for value in range(LOWER, UPPER + 1):
        print("{} {}".format(value, chr(value)))

def get_number(number):
    while number < int(LOWER) or number > int(UPPER):
        number = int(input("Enter a number between 33 and 127: "))
    return number


main()