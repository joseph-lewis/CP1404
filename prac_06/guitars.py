from prac_06.guitar import Guitar


def main():
    print("My guitars!")
    guitars = []
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = int(input("Cost: "))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(guitar_to_add, "added.")
        name = input("Name: ")
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    print("... snip ...")
    print("These are my guitars:")
    count = 0
    for guitar in guitars:
        count += 1
        vintage = ""
        if guitar.is_vintage():
            vintage = "(vintage)"
        print("Guitar {}: {:>20} ({}), worth $ {:10,.2f} {}".format(count, guitar.name, guitar.year, guitar.cost, vintage))


main()
