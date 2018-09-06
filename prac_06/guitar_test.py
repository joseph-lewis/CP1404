from prac_06.guitar import Guitar

def main():
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Another Guitar", 2012, 1000)
    print(guitar1)

    print("Gibson L-5 CES get_age() - Expected 96. Got ", guitar1.get_age())
    print("Another Guitar get_age() - Expected 6. Got ", guitar2.get_age())
    print("Gibson L-5 CES is_vintage() - Expected True. Got ", guitar1.is_vintage())
    print("Another Guitar is_vintage() - Expected False. Got ", guitar2.is_vintage())


main()
