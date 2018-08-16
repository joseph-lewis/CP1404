for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 110, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

stars = int(input("Enter number: "))
for i in range(stars):
    print('*', end=' ')
print()

stars = int(input("Enter number: "))
for i in range(stars):
    print('*' * (i + 1), end=' ')
    print()
print()
