
for i in range(1, 21, 2):
    print(i, end=' ')
print("\n")

print("a. Count in 10s from 0 to 100:")
for number in range(0, 101, 10):
    print(number, end=' ')
print("\n")

print("b. Count down from 20 to 1:")
for number in range(20, 0, -1):
    print(number, end=' ')
print("\n")

print("c. Print a number of stars:")
number_of_stars = int(input("Number of stars: "))
for _ in range(number_of_stars):
    print('*', end='')
print("\n")

print("d. Print lines of increasing stars:")
number_of_lines = int(input("Number of lines: "))
for line in range(1, number_of_lines + 1):
    print('*' * line)
