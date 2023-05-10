class Book:
    total_books = 0
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.total_books += 1
    
    @classmethod
    def get_total_books(cls):
        return cls.total_books
b1 = Book("The Catcher in the Rye", "J.D. Salinger")
b2 = Book("To Kill a Mockingbird", "Harper Lee")
print(Book.get_total_books())  # виведе 2
