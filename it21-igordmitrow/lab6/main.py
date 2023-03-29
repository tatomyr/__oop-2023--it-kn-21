class Dog:

    amount = 0
    woof = "Woof!"

    def __init__(self, name, age, breed, owner) -> None:
        self.name = name
        self.age = age
        self.breed = breed
        self.owner = owner
        Dog.amount += 1

    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old, {self.breed} breed, owner is {self.owner}"
    
    def bark(self):
        print(self.woof)
    
    def get_older(self):
        self.age += 1

    def get_age(self):
        return self.age
    
    def change_owner(self, new_owner):
        self.owner = new_owner

dog1 = Dog("Rex", 3, "Labrador", "Igor")
dog2 = Dog("Bob", 5, "Pitbull", "Igor")
dog3 = Dog("Jack", 2, "Poodle", "Igor")

# Рекс гавкає
dog2.bark()

# Виводимо вік третьої собаки та збільшуємо його на 1 рік
print(dog3.get_age())
dog3.get_older()
print(dog3.get_age())

# Змінюємо власника першої собаки
dog1.change_owner("Igor Dmitrow")

# Виводимо інформацію про першу собаку
print(dog1)

# Виводимо кількість створених собак
print("Кількість ініціалізованих собак: " + str(Dog.amount))
