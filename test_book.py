#
# test_book - This program tests the majority of the methods in the book class
#
# Author: 
# Version/Date: Winter 2024
#
import book

def main():
    # Create a list containing 3 books (test the constructor)
    book_list = []
    book_list.append(book.Book("978-0441172719", "Dune", "Frank Herbert", 2, True))
    book_list.append(book.Book("978-0375822742", "The City of Ember", "Jeanne DuPrau", 4, True))
    book_list.append(book.Book("978-0060513030", "Where the Sidewalk Ends", "Shel Silverstein", 9, False))

    # Test 1 
    # Get the first book in the list and borrow it
    # Then, using getters, display all information for this book
    current_book = book_list[0]
    current_book.borrow_it()
    print("*** Test 1 Output ***")
    print("ISBN:", current_book.get_isbn(),
          "\nTitle:", current_book.get_title(),
          "\nAuthor:", current_book.get_author(),
          "\nGenre:", current_book.get_genre_name(),
          "\nAvailability:", current_book.get_availability())
    
    # Test 2
    # Find all books with "city" in the title
    print("\n*** Test 2 Output ***")
    index = 0
    search_value = "city"
    while index < len(book_list):
        current_book = book_list[index]
        if search_value.lower() in current_book.get_title().lower():
            print("Found a match... Title:", current_book.get_title(),
                   ", ISBN:", current_book.get_isbn())
        index += 1

    # Test 3
    # Get the last book in the list and return it
    # Then, using setters, update the other information for this book
    current_book = book_list[-1]
    current_book.return_it()
    current_book.set_isbn("978-0394800165")
    current_book.set_title("Green Eggs and Ham")
    current_book.set_author("Dr. Seuss")
    current_book.set_genre(5)

    # Lastly, print report of all books (using implicit call to __str__())
    print("\n*** Test 3/Final Output ***")
    print("{:14s} {:25s} {:25s} {:20s} {:s}".format("ISBN", "Title",
        "Author", "Genre", "Availability"))
    for b in book_list:
        print(b)
        
if __name__ == "__main__":
    main()