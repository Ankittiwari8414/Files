# Task-1 Write a Python function to add a new book to the library. The book details should include title, author, and publication year. The details should be stored in a file called books.txt.
# Task -2 Write a function to search for a book by title in the books.txt file.
# Task-3 Write a function to display all books in the library from the books.txt file.
# Task-4  Write a function to delete a book from the books.txt file by its title.
# Task-5 Implement a system where users can borrow a book. Write a function that marks a book as borrowed in the books.txt file. Create a new file borrowed_books.txt to track borrowed books.
# Task-6 Write a function that marks a book as returned, updating both books.txt and borrowed_books.txt files.
# Task-7 Write a main program loop to manage the library system, allowing users to choose actions from a menu.


import os
def menu():
    print("Nsti book store")
    print("1. Add a book.")
    print("2. search for book")
    print("3. display all books")
    print("4.delete the book.")
    print("5. borrow the book")
    print("6.returned book")
    print("7. Exit")

def add_new_book(filename):
    try:
        with open(filename,"a") as file:
            title=input("Enter the book title:")
            author=input("Enter the name of author:")
            published=input("Enter the publication year of book:")
            book=f'{title},{author},{published}\n'
            file.write(book)
            print("Book added successfully.")
    except Exception as e:
        print(f'An Error Occurred;{e}')

def search_book(filename):
    try:
        if os.path.exists(filename):
            search=input("Enter the book name:")
        with open(filename,"r") as file:
            books=file.readlines()
            found=False
            for book in books:
                title,author,published=book.strip().split(',')
                if title==search:
                    print("Book found below.")
                    print(f"Title-{title}")
                    print(f"Author -{author}")
                    print(f"published year -{published}")
                    found=True
                    break
                if not found:
                    print("Book not found")
                else:
                    print("Inventory file does not exist.")
    except Exception as e:
        print(f"An error occurred:{e}")

def Display_all_book(filename):
    try:
        if os.path.exists(filename):
            with open(filename,"r") as file:
                books=file.readlines()
                if books:
                    print("Inventory")
                    for book in books:
                        title,author,published=book.strip().split(',')
                        print(f'Title: {title},Author is {author}, published in {published}')
                else:
                    print("Inventory file does not exits.")
    except Exception as e:
        print(f"An error Occurred. ")

def Del_book(filename):
    try:
        if os.path.exists(filename):
            title_to_delete = input("Enter the book name: ").lower()
            with open(filename, "r") as file:
                books = file.readlines()
            found = False
            with open(filename, "w") as file:
                for book in books:
                    title, author, published = book.strip().split(',')
                    if title.lower() == title_to_delete:
                        print(f"Deleted: {title}, Author: {author}, Publication Year: {published}")
                        found = True
                    else:
                        file.write(book)
            if not found:
                print("Book was not found in the library.")
        else:
            print("The file does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}") 

def Borrow_book(filename):
    try:
        if os.path.exists(filename):
            title_to_borrow = input("Enter the book name: ")
            with open(filename, "r") as file:
                books = file.readlines()

            found = False
            with open(filename, "w") as file:
                for book in books:
                    title, author, published = book.strip().split(',')

                    if title == title_to_borrow:
                        print(f"Book Borrowed: {title}, Author: {author}, Publication Year: {published}")
                        with open("borrowed_books.txt", "a") as borrowed_file:
                            borrowed_file.write(f"{title},{author},{published}\n")

                        found = True
                    else:
                        file.write(book)

            if not found:
                print("Book was not found in the library.")
        else:
            print("The file does not exist.")

    except Exception as e:
        print(f"An error occurred: {e}")

def Return_book(filename):
    try:
        borrowed_filename = "borrowed_books.txt"

        if os.path.exists(filename) and os.path.exists(borrowed_filename):
            title_to_return = input("Enter the book name to return: ")
            with open(borrowed_filename, "r") as borrowed_file:
                borrowed_books = borrowed_file.readlines()
            with open(filename, "r") as file:
                books = file.readlines()
            found = False
            with open(borrowed_filename, "w") as borrowed_file:
                for book in borrowed_books:
                    title, author, published = book.strip().split(',')
                    if title == title_to_return:
                        print(f"Book Returned: {title}, Author: {author}, Publication Year: {published}")
                        with open(filename, "a") as file_append:
                            file_append.write(f"{title},{author},{published}\n")

                        found = True
                    else:
                        borrowed_file.write(book)

            if not found:
                print("Book was not found in the borrowed books list.")
        else:
            print("One or both of the required files do not exist.")

    except Exception as e:
        print(f"An error occurred: {e}")

def menu():
    print("\nLibrary Management System")
    print("1. Add New Book")
    print("2. Search Book")
    print("3. Display All Books")
    print("4. Delete Book")
    print("5. Borrow Book")
    print("6. Return Book")
    print("7. Exit")

def main():
    filename = "books.txt"
    while True:
        menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_new_book(filename)
        elif choice == "2":
            search_book(filename)
        elif choice == "3":
            Display_all_book(filename)
        elif choice == "4":
            Del_book(filename)
        elif choice == "5":
            Borrow_book(filename)
        elif choice == "6":
            Return_book(filename)
        elif choice == "7":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
