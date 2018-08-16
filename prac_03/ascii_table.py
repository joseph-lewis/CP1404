LOWER = 33
UPPER = 127


char = input("Enter character: ")
print("The ASCII code for {} is {}".format(char, ord(char)))
number = int(input("Enter a number between 33 and 127: "))
while number < int(LOWER) or number > int(UPPER):
    number = int(input("Enter a number between 33 and 127: "))
print("The character for {} is {}".format(number, (chr(int(number)))))

for value in range(LOWER, UPPER + 1):
    print("{} {}".format(value, chr(value)))




