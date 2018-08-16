# file_open = open("name.txt", "w")
# users_name = str(input("Enter your name: "))
# print(users_name, file=file_open)
# file_open.close()

# file_out = open("name.txt", "r")
# print("Your name is: {}".format(file_out.read()))
# file_out.close()

# file_add_numbers = open("numbers.txt", "r")
# num1 = file_add_numbers.readline().strip()
# num2 = file_add_numbers.readline().strip()
# print(int(num1) + int(num2))

file_add_numbers = open("numbers.txt", "r")
total = 0
for i in file_add_numbers:
    num = int(i)
    total += num
print(total)
file_add_numbers.close()