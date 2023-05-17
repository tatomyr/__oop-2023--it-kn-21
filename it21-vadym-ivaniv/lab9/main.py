class Fruit:
    def __init__(self, name, age, breed, owner):
        self.name = name
        self.age = age
        self.breed = breed
        self.owner = owner

    def bite(self):
        print(self.name + ": Crunch!")

    def get_older(self):
        self.age += 1

    def get_age(self):
        return self.age

    def change_owner(self, new_owner):
        self.owner = new_owner

    def __repr__(self) -> str:
        return f"Fruit({self.name}, {self.age}, {self.breed}, {self.owner})"

    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old, {self.breed} breed, owner is {self.owner}"

    def __add__(self, other):
        return self.age + other.age

    def __sub__(self, other):
        return self.age - other.age

    def __len__(self):
        return len(self.name)


fruit = Fruit("Golden Delicious", 3, "Golden Delicious", "Vadym")
fruit1 = Fruit("Granny Smith", 5, "Granny Smith", "Vadym")

# Виводимо інформацію про фрукт
print(repr(fruit))
print(fruit)

# Додаємо вік фруктів і віднімаємо
print(fruit + fruit1)
print(fruit1 - fruit)

# Виводимо довжину імені фрукта
print(len(fruit))
