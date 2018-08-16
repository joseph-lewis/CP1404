"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        denominator = int(input("Enter a denominator other than zero: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# The ValueError will occur when a letter or something other than a
# number is entered
#
# ZeroDivisionError will occur when the denominator entered is a zero
#
# The only way to prevent the zero division error is through a loop that checks
# if it is a zero, and if it is then it will ask again until a valid number is entered