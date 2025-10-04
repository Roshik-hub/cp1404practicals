# files.py

# 1. Ask user for name, write to name.txt using open and close
name = input("Enter your name: ")
out_file = open("name.txt", "w")
out_file.write(name)
out_file.close()

# 2. Read name from name.txt and print greeting, using open and close
in_file = open("name.txt", "r")
stored_name = in_file.read().strip()
in_file.close()
print(f"Hi {stored_name}!")

# 3. Read first two numbers from numbers.txt, add and print sum (use with, readline)
with open("numbers.txt", "r") as numbers_file:
    first_num = int(numbers_file.readline().strip())
    second_num = int(numbers_file.readline().strip())
    print(first_num + second_num)  # Should print 59

# 4. Sum all numbers in numbers.txt and print total (use with and for line in file)
total = 0
with open("numbers.txt", "r") as numbers_file:
    for line in numbers_file:
        total += int(line.strip())
print(total)
