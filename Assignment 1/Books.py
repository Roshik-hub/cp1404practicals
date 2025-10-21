"""
CP1404 Assignment 1 - Books to Read
Name: Roshik Maharjan
Date Started: 20/10/2025
GitHub URL: https://github.com/YOURUSERNAME/assignment1
"""

FILENAME = "books.csv"

MENU = """Menu:
D - Display books
A - Add a new book
C - Complete a book
Q - Quit
>>> """


def main():
    """Main function to run the Books To Read program."""
    print("Books to Read 1.0 by Roshik Maharjan")
    books = load_books(FILENAME)
    print(f"{len(books)} books loaded.")

    # Display menu and handle user choices
    choice = input(MENU).lower()
    while choice != 'q':
        if choice == 'd':
            display_books(books)
        elif choice == 'a':
            add_book(books)
        elif choice == 'c':
            complete_book(books)
        else:
            print("Invalid menu choice")
        choice = input(MENU).lower()

    # Save books and exit
    save_books(FILENAME, books)
    print(f"{len(books)} books saved to {FILENAME}")
    print('"So many books, so little time. Frank Zappa"')


def load_books(filename):
    """Load books from a CSV file into a list of [title, author, pages, status]."""
    books = []
    with open(filename, "r") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            title, author, pages, status = parts[0], parts[1], int(parts[2]), parts[3]
            books.append([title, author, pages, status])
    return books


def save_books(filename, books):
    """Save the list of books back to the CSV file."""
    with open(filename, "w") as out_file:
        for book in books:
            print(f"{book[0]},{book[1]},{book[2]},{book[3]}", file=out_file)


def display_books(books):
    """Display the list of books, indicating unread ones with '*', and show total unread books/pages."""
    unread_books = 0
    unread_pages = 0
    for i, book in enumerate(books, 1):
        mark = "*" if book[3] == 'u' else " "
        print(f"{mark}{i}. {book[0]} by {book[1]} {book[2]} pages")
        if book[3] == 'u':
            unread_books += 1
            unread_pages += book[2]

    if unread_books == 0:
        print("No books left to read. Why not add a new book?")
    else:
        print(f"You still need to read {unread_pages} pages in {unread_books} books.")


def add_book(books):
    """Prompt user to enter book details, validate input, and add the book to the list."""
    # Title
    title = input("Title: ").strip()
    while title == "":
        print("Input can not be blank")
        title = input("Title: ").strip()

    # Author
    author = input("Author: ").strip()
    while author == "":
        print("Input can not be blank")
        author = input("Author: ").strip()

    # Pages
    pages_input = input("Number of Pages: ").strip()
    pages = get_valid_page_count(pages_input)

    books.append([title, author, pages, 'u'])
    print(f"{title} by {author} ({pages} pages) added.")


def get_valid_page_count(initial_input):
    """
        Validate and return a positive integer for number of pages.
        Keeps prompting the user until valid input is received.
    """
    pages_input = initial_input
    pages = 0
    valid = False
    while not valid:
        try:
            pages = int(pages_input)
            if pages <= 0:
                print("Number must be > 0")
                pages_input = input("Number of Pages: ").strip()
            else:
                valid = True
        except ValueError:
            print("Invalid input - please enter a valid number")
            pages_input = input("Number of Pages: ").strip()
    return pages


def complete_book(books):
    """
        Mark a book as completed based on user input.
        Only allows completion of unread books.
    """
    unread_books = [book for book in books if book[3] == 'u']
    if not unread_books:
        print("No unread books - well done!")
        return

    for i, book in enumerate(books, 1):
        mark = "*" if book[3] == 'u' else " "
        print(f"{mark}{i}. {book[0]} by {book[1]} {book[2]} pages")

    total_unread_pages = sum(book[2] for book in unread_books)
    print(f"You still need to read {total_unread_pages} pages in {len(unread_books)} books.")

    # Get valid book number input
    book_index = get_valid_book_number(books)
    if book_index is not None:
        books[book_index][3] = 'c'
        print(f"{books[book_index][0]} by {books[book_index][1]} completed!")


def get_valid_book_number(books):
    """
        Prompt the user for a valid book number to mark as complete.
        Ensures the number is within range and the book is not already completed.
        Returns the 0-based index of the selected book.
    """
    number = None
    valid_input = False
    while not valid_input:
        user_input = input("Enter the number of a book to mark as completed\n>>> ").strip()
        try:
            number = int(user_input)
            if number < 1:
                print("Number must be > 0")
            elif number > len(books):
                print("Invalid book number")
            elif books[number - 1][3] == 'c':
                print("That book is already completed")
            else:
                valid_input = True
        except ValueError:
            print("Invalid input - please enter a valid number")
    return number - 1

if __name__ == '__main__':
   main()
