class Book:
	def init(self, title, author, year_published, publisher):
	self.title = title
	self.author = author
	self.year_published = year_published
	self.publisher = publisher
	def __repr__(self):
		return f"Book({self.title}, {self.author}, {self.year_published}, {self.publisher})"

	def __str__(self):
		return f"{self.title} by {self.author}, published by {self.publisher} in {self.year_published}"

	def __add__(self, other):
		return self.year_published + other.year_published

	def __sub__(self, other):
		return self.year_published - other.year_published

	def __len__(self):
		return len(self.title)

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Charles Scribner's Sons")
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960, "J. B. Lippincott & Co.")

print(repr(book1))
print(book1)

print(book1 + book2)
print(book2 - book1)

print(len(book1))