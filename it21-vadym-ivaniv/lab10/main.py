class Fruit:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bite(self):
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

fruit = Fruit("Golden Delicious", 3)
fruit.bite()
print(fruit.age)
fruit.age = 4
print(fruit.age)
fruit.name = "Granny Smith"
print(fruit.name)
del fruit.name
