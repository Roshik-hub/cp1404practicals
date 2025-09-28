MIN_LENGTH = 6

def main():
    password = get_password()
    print_asterisks(password)


def get_password():
    password = input("Enter a password: ")
    while len(password) < MIN_LENGTH:
        print("Password too short")
        password = input("Enter a password: ")
    return password


def print_asterisks(password):
    print("*" * len(password))

main()
