"""
CP1404 Practical 07
Read, display, add, and save guitar information.
"""

from guitar import Guitar

def main():
    guitars = []

    # Load guitars from file (tab-separated)
    with open("guitars.csv", "r") as in_file:
        for line in in_file:
            parts = line.strip().split("\t")
            guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(guitar)

    # Display current guitars
    print("My guitars:")
    for g in guitars:
        print(g)

    # Sort guitars by year (oldest first)
    guitars.sort()
    print("\nGuitars sorted by year:")
    for g in guitars:
        print(g)

    # Add new guitars interactively
    while True:
        name = input("Enter guitar name (blank to stop): ")
        if name == "":
            break
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitars.append(Guitar(name, year, cost))

    # Save updated list back to file
    with open("guitars.csv", "w") as out_file:
        for g in guitars:
            out_file.write(f"{g.name}\t{g.year}\t{g.cost}\n")

main()
