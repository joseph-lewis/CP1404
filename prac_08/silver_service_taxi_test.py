from prac_08.silverservicetaxi import SilverServiceTaxi


def main():
    taxi = SilverServiceTaxi("Fancy Taxi", 100, 2)
    taxi.drive(18)
    print(taxi.get_fare())


main()