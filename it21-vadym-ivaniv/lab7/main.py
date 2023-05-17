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

    @classmethod
    def change_crunch(cls, new_crunch):
        cls.crunch = new_crunch

    @staticmethod
    def is_fruit_big(size):
        return size >= 3


fruit1 = Fruit("Apple", "Red", 3)
fruit2 = Fruit("Orange", "Orange", 2)
fruit3 = Fruit("Banana", "Yellow", 4)

# Виводимо інформацію про перший фрукт
print(fruit1)

fruit1.bite()

Fruit.change_crunch("Crunchy!")

fruit1.bite()

print(Fruit.is_fruit_big(5))

# Виводимо кількість створених фруктів
print("Кількість створених фруктів: " + str(Fruit.amount))
