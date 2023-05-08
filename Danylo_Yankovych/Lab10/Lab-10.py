class Dog:
    def __init__(self, name, age):
        self._name = None
        self._age = None
        self.name = name
        self.age = age

    def speak(self):
        print("Woof!")

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

dog = Dog("Boxer", 5)
dog.speak()
print(dog.age)
dog.age = 6
print(dog.age)
dog.name = "Sparky"
print(dog.name)
del dog.name