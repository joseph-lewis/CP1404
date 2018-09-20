from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.current_fare_distance = 0
        self.price_per_km = fanciness * Taxi.price_per_km

    def __str__(self):
        return "{}, {}km on current fare, ${:.2f}/km plus flagfall of ${:.2f}".format(super().__str__(),
                                                             self.current_fare_distance,
                                                             self.price_per_km, self.flagfall)

    def get_fare(self):
        return round(((self.price_per_km * self.current_fare_distance) + self.flagfall), 1)

