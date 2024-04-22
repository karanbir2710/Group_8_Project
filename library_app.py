from book import Book
import os

def load_books(book_list, file_path):
    with open(file_path, 'r') as file:
        for line in file:
            isbn, title, author, genre, available = line.strip().split(',')
            genre = int(genre)
            available = available.lower() == 'available'
            book_list.append(Book(isbn, title, author, genre, available))
    print("Book catalog has been loaded.")
    return len(book_list)


def print_menu(menu_heading, menu_options):
    print(menu_heading, "\n", "="*34)
    for key, value in menu_options.items():
        print(f"{key}: {value}")
    print_menu_flag = 0
    while print_menu_flag == 0:
        choice = input("Enter your selection: ")
        if choice.isdigit() and int(choice) in menu_options.keys():
            return int(choice)
        else:
            print("Invalid choice. Please try again.")

def search_books(book_list, search_string):
    search_results = []
    for book in book_list:
        if (search_string.lower() in book.get_isbn().lower() or
            search_string.lower() in book.get_title().lower() or
            search_string.lower() in book.get_author().lower() or
            search_string.lower() == book.get_genre_name().lower()):
            search_results.append(book)
        else:
            # Check if the search string matches any part of the genre name
            for word in search_string.lower().split():
                if word in book.get_genre_name().lower():
                    search_results.append(book)
                    break
    return search_results


def borrow_book(book_list):
    isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")
    index = find_book_by_isbn(book_list, isbn)
    if index is not None:  # Check if the book is found
        if book_list[index].get_availability() == "Available":
            # Borrow the book
            book_list[index].borrow_it()
            print(f'{book_list[index].get_title()} with ISBN {isbn} successfully borrowed.')
        else:
            print(f'{book_list[index].get_title()} with ISBN {isbn} is not currently available.')
    else:
        print("No book found with that ISBN.")





def find_book_by_isbn(book_list, isbn):
    index = 0
    for book in book_list:
        if book.get_isbn() == isbn:
            return index
        index += 1
    return None

def return_book(book_list, file_path):
    isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")
    index = find_book_by_isbn(book_list, isbn)
    if index is not None:  # Check if the book is found
        if book_list[index].get_availability() == "Borrowed":
            # Return the book
            book_list[index].return_it()
            print(f"'{book_list[index].get_title()}' with ISBN {isbn} successfully returned.")
            # Save the updated book list to the CSV file
            save_books(book_list, file_path)
        else:
            print(f"'{book_list[index].get_title()}' with ISBN {isbn} is not currently borrowed.")
    else:
        print("No book found with that ISBN.")


def add_book(book_list, file_path):  # Added file_path parameter
    isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")
    title = input("Enter title: ")
    author = input("Enter author name: ")
    
    valid_genre = False  # Flag variable to control the while loop
    while not valid_genre:
        genre_name = input("Enter genre: ")
        genre = -1
        for key, value in Book.GENRE_NAMES.items():
            if genre_name.lower() == value.lower():
                genre = key
                valid_genre = True  # Set the flag to True if a valid genre is found
                break
        if not valid_genre:
            print("Invalid genre. Choices are: Romance, Mystery, Science Fiction, Thriller, Young Adult, Children's Fiction, Self-help, Fantasy, Historical Fiction, Poetry.")

    book_list.append(Book(isbn, title, author, genre, True))
    save_books(book_list, file_path)  # Update the CSV file
    print(f"'{title}' with ISBN {isbn} successfully added.")


def remove_book(book_list, file_path):  
    isbn = input("Enter the ISBN of the book you want to remove: ")
    index = find_book_by_isbn(book_list, isbn)
    if index is not None:  # Check if the book is found
        title = book_list[index].get_title()
        book_list.remove(book_list[index])  # Remove the book from the list
        save_books(book_list, file_path)  # Update the CSV file
        print(f"'{title}' with ISBN {isbn} successfully removed.")
    else:
        print("No book found with that ISBN.")


def print_books(book_list):
    if book_list:
        print(f'{"ISBN":<14}{"Title":<35}{"Author":<25}{"Genre":<20}{"Availability":<15}')  # Adjusted the format
        for book in book_list:
            print(f"{book.get_isbn():<14}{book.get_title():<35}{book.get_author():<25}{book.get_genre_name():<20}{book.get_availability():<15}")  # Use getters to retrieve attributes
    else:
        print("No matching books found.")


def save_books(book_list, file_path):
    with open(file_path, 'w') as file:
        for book in book_list:
            availability = 'Available' if book.get_availability() else 'Borrowed'  # Ensure correct writing of availability
            file.write(f"{book.get_isbn()},{book.get_title()},{book.get_author()},{book.get_genre()},{availability}\n")
    return len(book_list)



def main():
    
    books = []
    print("Starting the system...")
    
    file_path = input("Enter book catalog filename: ")
    while not os.path.isfile(file_path):
        file_path = input(f"File not found. Re-enter book catalog filename: ")
    
    load_books(books, file_path)
    
    menu_heading = "\nReader's Guild Library - Main Menu"
    menu_options = {
        1: "Search for books",
        2: "Borrow a book",
        3: "Return a book",
        0: "Exit the system"
    }

    librarian_options = {
        4: "Add a book",
        5: "Remove a book",
        6: "Print catalog"
    }

    show_librarian_options = False
    
    choice = -1
    while choice != 0:
        print(menu_heading, "\n", "="*34)
        if not show_librarian_options:
            for key, value in menu_options.items():
                print(f"{key}: {value}")
        else:
            for key, value in menu_options.items():
                print(f"{key}: {value}")
            for key, value in librarian_options.items():
                print(f"{key}: {value}")

        choice = input("Enter your selection: ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 0:
                save_books(books, file_path)
                print("\n-- Exit the system --\nBook catalog has been saved.\nGood Bye!")
                break  # Exit the loop to end the program
            elif choice == 1:
                print("\n-- Search for books --")
                search_string = input("Enter search value: ")
                search_results = search_books(books, search_string)
                print_books(search_results)
            elif choice == 2:
                print("\n-- Borrow a book --")
                borrow_book(books)
            elif choice == 3:
                print("\n-- Return a book --")
                return_book(books, file_path)  # Added
            elif choice == 2130:  # Access librarian options
                show_librarian_options = True
            elif show_librarian_options and choice in librarian_options.keys():
               
                if choice == 4:
                    print("\n-- Add a book --")
                    add_book(books, file_path)
                elif choice == 5:
                    print("\n-- Remove a book --")
                    remove_book(books, file_path)
                elif choice == 6:
                    print("\n-- Print book catalog --")
                    print_books(books)
            else:
                print("Invalid option")
        else:
            print("Invalid option")
        print()



if __name__ == "__main__":
    main()



