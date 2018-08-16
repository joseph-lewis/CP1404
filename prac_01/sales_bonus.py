"""
Program to calculate and display a user's bonus based on sales.  
If sales are under $1,000, the user gets a 10% bonus.  
If sales are $1,000 or over, the bonus is 15%.  
"""


def main():

    sales = float(input("Enter Sales: "))
    if sales < 1000:
        bonus = 0.1 * sales
        print("Your bonus is: $", bonus)
    else:
        bonus = 0.15 * sales
        print("Your bonus is: $", bonus)


main()
