"""
CP1404 Practical
Cumulative total income program with improved structure and formatting
"""


def main():
    """Get incomes and display the income report."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print_income_report(incomes)


def print_income_report(incomes):
    """Display income report showing monthly and cumulative totals."""
    print("\nIncome Report\n-------------")
    total = 0
    for month, income in enumerate(incomes, start=1):
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")


main()
