import random

class Animal:

    def __init__(self, name, age, breed, owner):
        self.name = name
        self.age = age
        self.breed = breed
        self.owner = owner

    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old, {self.breed} breed, owner is {self.owner}"
    
    def get_older(self):
        self.age += 1

    def get_age(self):
        return self.age
    
    def change_owner(self, new_owner):
        self.owner = new_owner

class Dog(Animal):

    woof = "Woof!"

    def __init__(self, name, age, breed, owner):
        super().__init__(name, age, breed, owner)

    def bark(self):
        print(self.name + ": " + self.woof)


class Cat(Animal):
    
    meow = "Meow!"

    def __init__(self, name, age, breed, owner, hamster=None):
        super().__init__(name, age, breed, owner)
        self.hamster = hamster

    def meow(self):
        print(self.name + ": " + self.meow)

    def eat_hamster(self):
        if self.hamster is not None:
            if self.hamster.willSurvive():
                print(self.name + " tried to eat " + self.hamster.name + " but it survived")
                return
            print(self.name + " ate " + self.hamster.name)
            del self.hamster
        else:
            print(self.name + " has no hamster to eat")


class Hamster(Animal):
    
    squeak = "Squeak!"

    def __init__(self, name, age, breed, owner, luckiness=0):
        super().__init__(name, age, breed, owner)
        self.luckiness = luckiness

    def squeak(self):
        print(self.name + ": " + self.squeak)

    def willSurvive(self):
        return 1 - random.random() <= self.luckiness

    def __del__(self):
        print(self.name + " died")

dog = Dog("Rex", 3, "Labrador", "ID")
hamster = Hamster("Jerry", 1, "Syrian", "ID", 0.5)
cat = Cat("Tom", 2, "Persian", "ID", hamster)

print(isinstance(dog, Cat)) # False
print(isinstance(dog, Animal)) # True
print(isinstance(dog, Dog)) # True

print(issubclass(Dog, Animal)) # True
print(issubclass(Cat, Dog)) # False

cat.eat_hamster()

dog.bark()
print(cat)

