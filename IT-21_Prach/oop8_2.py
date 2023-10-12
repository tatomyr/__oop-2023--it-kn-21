class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def make_sound(self):
        pass

class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def make_sound(self):
        print("Meow!")
    
    def hunt(self, dog):
        print(f"{self.name} is hunting")
        dog.eat()
    
class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def make_sound(self):
        print("Woof!")
    
    def eat(self):
        print(f"{self.name} is eating")

cat = Cat("Whiskers", 2)
dog = Dog("Buddy", 4)

cat.hunt(dog)
