"""
Wimbledon Champions
Estimate: 30 minutes
Actual:   (fill in after finishing)
"""


def read_wimbledon_file(filename):
    """Read CSV file and return a list of lists (rows)"""
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        next(in_file)  # skip header
        for line in in_file:
            parts = line.strip().split(",")  # split by comma
            data.append(parts)  # [year, champion, country]
    return data


def count_champions(data):
    """Return a dictionary of champions and how many times they have won"""
    champion_counts = {}
    for row in data:
        champion = row[1]
        if champion in champion_counts:
            champion_counts[champion] += 1
        else:
            champion_counts[champion] = 1
    return champion_counts


def get_countries(data):
    """Return a set of unique countries from the data"""
    countries = set()
    for row in data:
        countries.add(row[2])
    return countries


def main():
    filename = "wimbledon.csv"
    data = read_wimbledon_file(filename)

    champions = count_champions(data)
    countries = get_countries(data)

    print("Wimbledon Champions:")
    for champion, wins in champions.items():
        print(f"{champion} {wins}")

    sorted_countries = sorted(countries)
    print("\nThese", len(sorted_countries), "countries have won Wimbledon:")
    print(", ".join(sorted_countries))


main()
