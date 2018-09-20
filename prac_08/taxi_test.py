from prac_08.taxi import Taxi

def main():
    taxi = Taxi("Prius 1", 100)
    taxi.drive(40)
    print(taxi)
    print("${:.2f}".format(taxi.get_fare()))

main()
