class Bird():
    def __init__(self, name, age, species, owner):
        self.name = name
        self.age = age
        self.species = species
        self.owner = owner

    def chirp(self):
        print(self.name + ": Chirp chirp!")

    def get_older(self):
        self.age += 1

    def get_age(self):
        return self.age

    def change_owner(self, new_owner):
        self.owner = new_owner

    def __repr__(self) -> str:
        return f"Bird({self.name}, {self.age}, {self.species}, {self.owner})"
    
    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old, {self.species} species, owner is {self.owner}"
    
    def __add__(self, other):
        return self.age + other.age
    
    def __sub__(self, other):
        return self.age - other.age
    
    def __len__(self):
        return len(self.name)
    

bird = Bird("Polly", 2, "Parrot", "John")
bird1 = Bird("Kiwi", 1, "Kiwi", "Sarah")

# Виводимо інформацію про птаха
print(repr(bird))
print(bird)

# Додаємо вік птахів і віднімаємо
print(bird + bird1)
print(bird1 - bird)

# Виводимо довжину імені птаха
print(len(bird))