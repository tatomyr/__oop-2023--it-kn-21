class Dog:
    amount = 0
    woof = "Woof!"

    def __init__(self, name, age, breed, owner):
        self.name = name
        self.age = age
        self.breed = breed
        self.owner = owner
        Dog.amount += 1

    def __str__(self):
        return f"{self.name} is {self.age} years old, {self.breed} breed, owner is {self.owner}"

    def bark(self):
        print(self.woof)

    def get_older(self):
        self.age += 1

    def get_age(self):
        return self.age

    def change_owner(self, new_owner):
        self.owner = new_owner


dog1 = Dog("Boxer", 3, "Bulldog", "Danylo")
dog2 = Dog("Goldy", 5, "Golden Retriever", "Danylo")
dog3 = Dog("Snowy", 2, "Husky", "Danylo")

# Goldy гавкає
dog2.bark()

# Виводимо вік Snowy та збільшуємо його на 1 рік
age = dog3.get_age()
print(age)
dog3.get_older()
print(dog3.get_age())

dog1.change_owner("Danylo Yankovych")

print(dog1)

print(f"Кількість ініціалізованих собак: {Dog.amount}")