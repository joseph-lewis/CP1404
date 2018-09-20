from prac_08.taxi import Taxi
from prac_08.silverservicetaxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"

def main():
    print("Let's drive!")
    print(MENU)
    menu_choice = input(">>> ")
    bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    taxi_choice = None
    while menu_choice != "q":
        if menu_choice == "c":
            print("Taxis Available:")
            taxi_count = 0
            for taxi in taxis:
                print("{} - {}".format(taxi_count, taxi))
                taxi_count += 1
            taxi_choice = int(input("Choose Taxi: "))
        if menu_choice == "d":
            if taxi_choice is None:
                print("You need to choose a taxi first")
            else:
                distance = int(input("Drive how far? "))
                taxi_chosen = taxis[taxi_choice]
                taxi_chosen.drive(distance)
                print("Your {} trip cost you ${:.2f}".format(taxi_chosen.name, taxi_chosen.get_fare()))
                bill += taxi_chosen.get_fare()
        print("Bill to Date: ${:.2f}".format(bill))
        print(MENU)
        menu_choice = input(">>> ")
    print("Total trip cost: ${:.2f}".format(bill))
    for taxi in taxis:
        print(taxi)
main()
