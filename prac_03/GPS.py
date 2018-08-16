import random

def main():
    year_count = 1
    population = 1000
    print("Welcome to the Gopher Population Simulator! \nStarting population: {} \nYear {}".format(population, year_count))
    while year_count < 10:
        birth_rate = random.uniform(0.1, 0.2) * population
        death_rate = random.uniform(0.05, 0.25) * population
        population = population + birth_rate - death_rate
        year_count += 1
        print("{} gophers were born. {} died.\nPopulation: {} \nYear {}\n".format(int(birth_rate), int(death_rate), int(population), year_count))
main()
