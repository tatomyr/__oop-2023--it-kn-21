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

class Bird(Animal):

    chirp = "Chirp!"

    def __init__(self, name, age, breed, owner):
        super().__init__(name, age, breed, owner)

    def chirp(self):
        print(self.name + ": " + self.chirp)

    def eat_spider(self):
        if self.spider is not None:
            if self.spider.willSurvive():
                print(self.name + " tried to eat " + self.spider.name + " but it survived")
                return
            print(self.name + " ate " + self.spider.name)
            del self.spider
        else:
            print(self.name + " has no spider to eat")


class Monkey(Animal):
    
    sound = "U-a-a!"

    def __init__(self, name, age, breed, owner, spider=None):
        super().__init__(name, age, breed, owner)
        self.monkey = monkey

    def sound(self):
        print(self.name + ": " + self.sound)



class Spider(Animal):
    
    sound = "Hshh!"

    def __init__(self, name, age, breed, owner, luckiness=0):
        super().__init__(name, age, breed, owner)
        self.luckiness = luckiness

    def sound(self):
        print(self.name + ": " + self.sound)

    def willSurvive(self):
        return 1 - random.random() <= self.luckiness

    def __del__(self):
        print(self.name + " died")

monkey = Monkey("Albert", 3, "Mandrill", "John")
spider = Spider("Spidy", 1, "Wasp", "James", 0.5)
bird = Bird("Rio", 2, "Canary", "Petra", spider)

print(isinstance(bird, Monkey)) # False
print(isinstance(bird, Animal)) # True
print(isinstance(bird, Bird)) # True

print(issubclass(Bird, Animal)) # True
print(issubclass(Monkey, Bird)) # False

cat.eat_spider()

bird.chirp()
print(monkey)

