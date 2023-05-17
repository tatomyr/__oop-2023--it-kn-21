class Apple:
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
        return f"Apple({self.name}, {self.age}, {self.breed}, {self.owner})"

    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old, {self.breed} breed, owner is {self.owner}"

    def __add__(self, other):
        return self.age + other.age

    def __sub__(self, other):
        return self.age - other.age

    def __len__(self):
        return len(self.name)


apple = Apple("Golden Delicious", 3, "Golden Delicious", "Vadym")
apple1 = Apple("Granny Smith", 5, "Granny Smith", "Vadym")

# Виводимо інформацію про яблуко
print(repr(apple))
print(apple)

# Додаємо вік яблук і віднімаємо
print(apple + apple1)
print(apple1 - apple)

# Виводимо довжину імені яблука
print(len(apple))
