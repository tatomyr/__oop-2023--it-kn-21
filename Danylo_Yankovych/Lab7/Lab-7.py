class Book:
    amount = 0
    genre = "Unknown"
    default_author = "Unknown"
    def __init__(self, title, author, year, pages, publisher):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages
        self.publisher = publisher
        Book.amount += 1

    def __str__(self):
        return f"{self.title} by {self.author}, published by {self.publisher} in {self.year}, {self.pages} pages"

    def get_published_year(self):
        return self.year

    def set_author(self, new_author):
        self.author = new_author

    def set_publisher(self, new_publisher):
        self.publisher = new_publisher

    @classmethod
    def from_dict(cls, dict):
        title, author, year, pages, publisher = dict.values()
        return cls(title, author, year, pages, publisher)

    @classmethod
    def set_genre(cls, new_genre):
        cls.genre = new_genre

    @staticmethod
    def is_long_book(pages):
        return pages >= 500

book1 = Book.from_dict({"title": "Harry Potter and the Philosopher's Stone", "author": "J.K. Rowling", "year": 1997, "pages": 223, "publisher": "Bloomsbury Publishing"})

print(book1)

print(Book.is_long_book(700))

Book.set_genre("Fantasy")

book1.set_author("Joanne Rowling")
book1.set_publisher("Scholastic")

print("Number of initialized books: " + str(Book.amount))