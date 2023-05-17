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


apple1 = Apple("Red", "Medium")
apple2 = Apple("Green", "Small")
apple3 = Apple("Yellow", "Large")

# Перше яблуко хрумкає
apple1.bite()

# Виводимо розмір третього яблука та збільшуємо його на 1
print(apple3.get_size())
apple3.grow()
print(apple3.get_size())

# Виводимо інформацію про перше яблуко
print(apple1)

# Виводимо кількість створених яблук
print("Кількість створених яблук: " + str(Apple.amount))