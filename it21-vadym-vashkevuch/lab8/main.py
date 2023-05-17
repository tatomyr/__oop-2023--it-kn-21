class Fruit:
    def __init__(self, name, ripeness):
        self.name = name
        self.ripeness = ripeness

    def __str__(self):
        return f"{self.name} is {self.ripeness}"

    def get_ripeness(self):
        return self.ripeness

    def change_ripeness(self, new_ripeness):
        self.ripeness = new_ripeness

class Apple(Fruit):
    crunch = "Crunch!"

    def __init__(self, name, ripeness):
        super().__init__(name, ripeness)

    def bite(self):
        print(self.name + ": " + self.crunch)

class Pear(Fruit):
    juicy = "Juicy!"

    def __init__(self, name, ripeness):
        super().__init__(name, ripeness)

    def bite(self):
        print(self.name + ": " + self.juicy)

class Apricot(Fruit):
    soft = "Soft!"

    def __init__(self, name, ripeness):
        super().__init__(name, ripeness)

    def bite(self):
        print(self.name + ": " + self.soft)

apple = Apple("Golden Delicious", "Ripe")
pear = Pear("Bartlett", "Juicy")
apricot = Apricot("Moorpark", "Soft")

print(isinstance(apple, Pear)) # False
print(isinstance(apple, Fruit)) # True
print(isinstance(apple, Apple)) # True

print(issubclass(Apple, Fruit)) # True
print(issubclass(Pear, Apple)) # False

apple.bite()
print(pear)
