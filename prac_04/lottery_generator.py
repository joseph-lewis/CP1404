import random
NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45

count = int(input("How many quick picks? "))
for i in range(count):
    print("{}  {}  {}  {}  {}  {}".format(random.randrange(1, 45), random.randrange(1, 45), random.randrange(1, 45), random.randrange(1, 45), random.randrange(1, 45), random.randrange(1, 45)))
