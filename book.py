class Book:
    
    # Constructor method to initialize attributes
    def __init__(self, isbn, title, author, genre, available):
        self.__isbn = isbn
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__available = available
    GENRE_NAMES = {
        0: "Romance",
        1: "Mystery",
        2: "Science Fiction",
        3: "Thriller",
        4: "Young Adult",
        5: "Children's Fiction",
        6: "Self-help",
        7: "Fantasy",
        8: "Historical Fiction",
        9: "Poetry"
    }
    # Getter methods for all attributes
    def get_isbn(self):
        return self.__isbn

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_genre(self):
        return self.__genre

    def get_available(self):
        return self.__available

    # Getter method to return genre name based on genre number
    def get_genre_name(self):
        genre_names = ["Romance", "Mystery", "Science Fiction", "Thrills",
                       "Young Adult", "Children's Fiction", "Self-help",
                       "Fantasy", "Historical Fiction", "Poetry"]
        return genre_names[self.__genre] if 0 <= self.__genre < len(genre_names) else "Unknown"

    # Getter method to return availability status as string
    def get_availability(self):
        return "Available" if self.__available else "Borrowed"

    # Setter methods for isbn, title, author, and genre
    def set_isbn(self, isbn):
        self.__isbn = isbn

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def set_genre(self, genre):
        self.__genre = genre

    # Method to mark the book as borrowed
    def borrow_it(self):
        self.__available = False

    # Method to mark the book as returned
    def return_it(self):
        self.__available = True

    # String representation of the book
    def __str__(self):
        return "{:14s} {:25s} {:25s} {:20s} {:s}".format(self.__isbn, self.__title,
                                                          self.__author, self.get_genre_name(),
                                                          self.get_availability())
