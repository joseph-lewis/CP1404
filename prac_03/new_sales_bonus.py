def main():

    sales = float(input("Enter Sales: "))
    sales_loop(sales)


def sales_loop(sales):
    while sales >= 0:
        if sales < 1000:
            bonus = 0.1 * sales
        else:
            bonus = 0.15 * sales
        print("Your bonus is: $", bonus)
        sales = float(input("Enter Sales: "))


main()
