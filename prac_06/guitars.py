"""
CP1404/CP5632 Practical - Playing with Guitars
"""

from guitar import Guitar

def main():
    print("My guitars!")
    guitars = []

    # Uncomment these lines for testing without typing input
    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.90))

    # User input loop
    while True:
        name = input("Name: ")
        if not name:  # blank name ends input
            break
        try:
            year = int(input("Year: "))
            cost = float(input("Cost: $"))
        except ValueError:
            print("Invalid input. Please enter numeric values for year and cost.")
            continue
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added.\n")

    # Print all guitars
    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")

main()