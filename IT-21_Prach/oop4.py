class Dog:
    species = "Canis lupus familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f"{self.name} is {self.age} years old"

my_dog = Dog("Fido", 3)

print(my_dog.name) # Виведе "Fido"
print(my_dog.age) # Виведе 3
print(my_dog.species) # Виведе "Canis lupus familiaris"
