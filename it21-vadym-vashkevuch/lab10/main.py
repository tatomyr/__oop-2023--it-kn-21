class Apple:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("Crunch!")

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value

    @name.deleter
    def name(self):
        del self._name
        print("Name deleted")

apple = Apple("Golden Delicious", 3)
apple.speak()
print(apple.age)
apple.age = 4
print(apple.age)
apple.name = "Granny Smith"
print(apple.name)
del apple.name
