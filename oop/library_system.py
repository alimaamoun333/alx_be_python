# library_system.py

class Book:
    """
    Base class representing a generic book.
    Attributes:
        title (str): Title of the book.
        author (str): Author of the book.
    """

    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __str__(self) -> str:
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """
    Electronic book subclass with additional file_size attribute.
    Attributes:
        file_size (int): Size of the ebook file in KB.
    """

    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self) -> str:
        return (f"EBook: {self.title} by {self.author}, "
                f"File Size: {self.file_size}KB")


class PrintBook(Book):
    """
    Printed book subclass with additional page_count attribute.
    Attributes:
        page_count (int): Number of pages in the printed book.
    """

    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self) -> str:
        return (f"PrintBook: {self.title} by {self.author}, "
                f"Page Count: {self.page_count}")


class Library:
    """
    Library class demonstrating composition.
    Manages a collection of Book, EBook, and PrintBook instances.
    """

    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        """
        Adds any Book-derived instance to the library.
        """
        self.books.append(book)

    def list_books(self):
        """
        Prints details of every book in the library.
        """
        if not self.books:
            print("Library is empty.")
            return

        for book in self.books:
            print(book)
