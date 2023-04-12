class Dog():
    def __init__(self, name, age, breed, owner):
        self.name = name
        self.age = age
        self.breed = breed
        self.owner = owner

    def bark(self):
        print(self.name + ": Woof!")

    def get_older(self):
        self.age += 1

    def get_age(self):
        return self.age

    def change_owner(self, new_owner):
        self.owner = new_owner

    def __repr__(self) -> str:
        return f"Dog({self.name}, {self.age}, {self.breed}, {self.owner})"
    
    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old, {self.breed} breed, owner is {self.owner}"
    
    def __add__(self, other):
        return self.age + other.age
    
    def __sub__(self, other):
        return self.age - other.age
    
    def __len__(self):
        return len(self.name)
    

dog = Dog("Rex", 3, "Labrador", "ID")
dog1 = Dog("Jack", 5, "Pitbull", "Igor")

# Виводимо інформацію про собаку
print(repr(dog))
print(dog)

# Додаємо вік собак і віднімаємо
print(dog + dog1)
print(dog1 - dog)

# Виводимо довжину імені собаки
print(len(dog))