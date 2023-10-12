class Book:
    def __init__(self, title, year):
        self._title = None
        self._year = None
        self.title = title
        self.year = year

    def speak(self):
        print("I am a book!")

    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, value):
        if value < 0:
            raise ValueError("Year cannot be negative")
        self._year = value
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if not value:
            raise ValueError("Title cannot be empty")
        self._title = value

    @title.deleter
    def title(self):
        del self._title
        print("Title deleted")

book = Book("To Kill a Mockingbird", 1960)
book.speak()
print(book.year)
book.year = 1961
print(book.year)
book.title = "Pride and Prejudice"
print(book.title)
del book.title
