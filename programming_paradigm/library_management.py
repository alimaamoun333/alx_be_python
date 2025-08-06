class Book:
    """
    Represents a single book in the library.
    title and author are public attributes.
    _is_checked_out is a private flag tracking availability.
    """

    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self) -> bool:
        """
        Mark this book as checked out if it’s currently available.
        Returns True on success, False if it was already checked out.
        """
        if self._is_checked_out:
            return False
        self._is_checked_out = True
        return True

    def return_book(self) -> bool:
        """
        Mark this book as returned if it’s currently checked out.
        Returns True on success, False if it wasn’t checked out.
        """
        if not self._is_checked_out:
            return False
        self._is_checked_out = False
        return True

    def is_available(self) -> bool:
        """
        True if the book is not checked out.
        """
        return not self._is_checked_out


class Library:
    """
    Manages a collection of Book instances.
    """

    def __init__(self):
        # _books holds all Book objects in this library
        self._books: list[Book] = []

    def add_book(self, book: Book) -> None:
        """
        Add a new Book to the library’s collection.
        """
        self._books.append(book)

    def check_out_book(self, title: str) -> bool:
        """
        Find the first available book matching `title` and check it out.
        Returns True if successful, False if no available copy is found.
        """
        for book in self._books:
            if book.title == title and book.is_available():
                return book.check_out()
        return False

    def return_book(self, title: str) -> bool:
        """
        Find the first checked-out book matching `title` and return it.
        Returns True if successful, False if no such copy is checked out.
        """
        for book in self._books:
            if book.title == title and not book.is_available():
                return book.return_book()
        return False

    def list_available_books(self) -> None:
        """
        Print all books that are currently not checked out.
        """
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
