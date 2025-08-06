# book_class.py

class Book:
    """
    A class representing a book, enhanced with magic methods:
    - __init__ to set title, author, year
    - __del__ to announce deletion
    - __str__ for user-friendly display
    - __repr__ for unambiguous, evaluable representation
    """

    def __init__(self, title: str, author: str, year: int):
        """
        Constructor: initialize title, author, and publication year.
        """
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        """
        String representation for end users.
        Format: "(title) by (author), published in (year)"
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self) -> str:
        """
        Official representation – should recreate the object when passed to eval().
        Format: "Book('title', 'author', year)"
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        """
        Destructor: called when the instance is about to be destroyed.
        Prints a message indicating which book is being deleted.
        """
    def __str__(self) -> str:
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self) -> str:
         return f"Book('{self.title}', '{self.author}', {self.year})"

    print(f"Deleting {self.title}")
