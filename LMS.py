library = {
    "Python Basics": {
        "author": "Rohan",
        "available": True,
        "issued_to": None
    },
    "Data Science": {
        "author": "Gupta",
        "available": True,
        "issued_to": None
    }
}

credentials = {
    "admin": "admin123",
    "librarian": "lib123"
}

current_user = None


# SIGN UP

def signup():

    print("\nSign Up")

    while True:

        username = input("Create username (0 to cancel): ").strip().lower()

        if username == "0":
            print("Cancelled.")
            return

        if username in credentials:
            print("Username already exists.")
        else:
            break

    password = input("Create password: ").strip()

    credentials[username] = password

    print("Account created.")


# LOGIN

def login():

    global current_user

    attempts = 3

    while attempts > 0:

        username = input("Username: ").strip().lower()
        password = input("Password: ").strip()

        if username in credentials and credentials[username] == password:

            current_user = username

            print(f"\nWelcome, {username}!")
            return True

        attempts -= 1

        print(f"Wrong username or password. Attempts left: {attempts}")

    print("Too many wrong attempts.")
    return False


# AUTH MENU

def authentication():

    while True:

        print("\n===== Library Management System =====")
        print("1. Sign Up")
        print("2. Login")
        print("3. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":

            signup()

        elif choice == "2":

            if login():
                return True

        elif choice == "3":

            print("Goodbye.")
            return False

        else:

            print("Please enter a valid option.")


# VIEW BOOKS

def display_books():

    if len(library) == 0:

        print("\nNo books found.")
        return

    print("\nBooks in Library:")

    for title, details in library.items():

        status = "Available" if details["available"] else "Issued"

        print(f"\nTitle : {title}")
        print(f"Author: {details['author']}")
        print(f"Status: {status}")

        if not details["available"]:
            print(f"Issued To: {details['issued_to']}")


# ADD BOOK

def add_book():

    title = input("\nEnter book title (0 to cancel): ").strip()

    if title == "0":
        print("Cancelled.")
        return

    title = title.title()

    for book in library:

        if book.lower() == title.lower():

            print("This book is already in the library.")
            return

    author = input("Enter author name (0 to cancel): ").strip()

    if author == "0":
        print("Cancelled.")
        return

    author = author.title()

    library[title] = {
        "author": author,
        "available": True,
        "issued_to": None
    }

    print("Book added.")


# ISSUE BOOK

def issue_book():

    global current_user

    available_books = {}

    print("\nAvailable Books:")

    count = 1

    for title, details in library.items():

        if details["available"]:

            available_books[str(count)] = title

            print(f"{count}. {title} by {details['author']}")

            count += 1

    if len(available_books) == 0:

        print("No books available.")
        return

    print("0. Cancel")

    choice = input("\nSelect book number: ").strip()

    if choice == "0":

        print("Cancelled.")
        return

    if choice not in available_books:

        print("Please enter a valid number.")
        return

    selected_book = available_books[choice]

    library[selected_book]["available"] = False
    library[selected_book]["issued_to"] = current_user

    print(f"\nYou have issued '{selected_book}'.")


# RETURN BOOK

def return_book():

    global current_user

    issued_books = {}

    print("\nYour Issued Books:")

    count = 1

    for title, details in library.items():

        if (
            not details["available"]
            and details["issued_to"] == current_user
        ):

            issued_books[str(count)] = title

            print(f"{count}. {title} by {details['author']}")

            count += 1

    if len(issued_books) == 0:

        print("You haven't issued any books yet.")
        return

    print("0. Cancel")

    choice = input("\nSelect book number to return: ").strip()

    if choice == "0":

        print("Cancelled.")
        return

    if choice not in issued_books:

        print("Please enter a valid number.")
        return

    selected_book = issued_books[choice]

    library[selected_book]["available"] = True
    library[selected_book]["issued_to"] = None

    print(f"\n'{selected_book}' returned.")


# VIEW ISSUED BOOKS

def view_issued_books():

    found = False

    print("\nIssued Books:")

    for title, details in library.items():

        if not details["available"]:

            found = True

            print(f"\nTitle : {title}")
            print(f"Author: {details['author']}")
            print(f"Issued To: {details['issued_to']}")

    if not found:

        print("No issued books found.")


# MAIN MENU

def main():

    while True:

        print("\n===== Main Menu =====")

        if current_user:
            print(f"Logged in as: {current_user}")

        print("\n1. View Books")
        print("2. Add Book")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. View Issued Books")
        print("6. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":

            display_books()

        elif choice == "2":

            add_book()

        elif choice == "3":

            issue_book()

        elif choice == "4":

            return_book()

        elif choice == "5":

            view_issued_books()

        elif choice == "6":

            print("\nThanks for using the Library System.")
            break

        else:

            print("Please enter a valid option.")


# START PROGRAM

print("Welcome to the Library Management System")

if authentication():
    main()
