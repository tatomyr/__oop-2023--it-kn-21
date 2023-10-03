class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            value = self.data[self.index]
            self.index += 1
            return value
        raise StopIteration

class MyCollection:
    def __init__(self):
        self.data = []

    def add_item(self, item):
        self.data.append(item)

    def create_iterator(self):
        return MyIterator(self.data)

# Використання паттерна "Ітератор"
collection = MyCollection()
collection.add_item("Item 1")
collection.add_item("Item 2")
collection.add_item("Item 3")

iterator = collection.create_iterator()

for item in iterator:
    print(item)

# Виведе:
# Item 1
# Item 2
# Item 3
