class Apple:

    amount = 0
    crunch = "Crunch!"

    def __init__(self, color, size):
        self.color = color
        self.size = size
        Apple.amount += 1

    def __str__(self):
        return f"Apple color: {self.color}, size: {self.size}"

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
    def is_apple_big(size):
        return size >= 3

apple1 = Apple("Red", 3)

# Виводимо інформацію про перше яблуко
print(apple1)

apple1.bite()

Apple.change_crunch("Crunchy!")

apple1.bite()

print(Apple.is_apple_big(5))

# Виводимо кількість створених яблук
print("Кількість створених яблук: " + str(Apple.amount))
