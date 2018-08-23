import random
NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45

count = int(input("How many quick picks? "))

for i in range(count):
    quickpick_lines = []
    for n in range(NUMBERS_PER_LINE):
        k = random.randrange(MINIMUM, MAXIMUM)
        while k in quickpick_lines:
            k = random.randrange(MINIMUM, MAXIMUM)
        quickpick_lines.append(k)
    quickpick_lines.sort()
    print(" ".join("{:2}".format(num) for num in quickpick_lines))


