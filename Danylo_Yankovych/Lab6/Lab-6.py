class Book:
    amount = 0

    def __init__(self, title, author, year, genre, pages):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.pages = pages
        Book.amount += 1

    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}. Genre: {self.genre}. {self.pages} pages."

    def get_pages(self):
        return self.pages

    def set_author(self, new_author):
        self.author = new_author

    def set_genre(self, new_genre):
        self.genre = new_genre

book1 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 1997, "Fantasy", 223)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction", 281)
book3 = Book("The Lord of the Rings", "J.R.R. Tolkien", 1954, "Fantasy", 1178)

# ƒрукуЇмо книгу book2
print(book2)

# «м≥нюЇмо автора book1
book1.set_author("Joanne Rowling")
print(book1)

# «м≥нюЇмо жанр book3
book3.set_genre("High fantasy")
print(book3)

print(f" ≥льк≥сть ≥н≥ц≥ал≥зованих книг: {Book.amount}")
