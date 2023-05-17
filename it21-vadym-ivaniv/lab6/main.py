class Fruit:
    amount = 0
    crunch = "Crunch!"

    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size
        Fruit.amount += 1

    def __str__(self):
        return f"{self.name} color: {self.color}, size: {self.size}"

    def bite(self):
        print(self.crunch)

    def grow(self):
        self.size += 1

    def get_size(self):
        return self.size


apple = Fruit("Apple", "Red", "Medium")
orange = Fruit("Orange", "Orange", "Large")
banana = Fruit("Banana", "Yellow", "Small")

# Перше яблуко хрумкає
apple.bite()

# Виводимо розмір третього фрукта та збільшуємо його на 1
print(orange.get_size())
orange.grow()
print(orange.get_size())

# Виводимо інформацію про перший фрукт
print(apple)

# Виводимо кількість створених фруктів
print("Кількість створених фруктів: " + str(Fruit.amount))
