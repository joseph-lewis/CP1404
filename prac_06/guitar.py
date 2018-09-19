class Guitar:
    def __init__(self, name="", year=0, cost=float):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : ${}".format(self.name, self.year, self.cost)

    def get_age(self):
        return 2018 - self.year

    def is_vintage(self):
        return self.get_age() >= 50
