class Bird:
    amount = 0
    chirp = "Chirp!"

    def __init__(self, name, age, species, owner):
        self.name = name
        self.age = age
        self.species = species
        self.owner = owner
        Bird.amount += 1

    def __str__(self):
        return f"{self.name} is a {self.species}, {self.age} years old, owned by {self.owner}"

    def chirp_sound(self):
        print(self.name + ": " + self.chirp)

    def get_older(self):
        self.age += 1

    def get_age(self):
        return self.age

    def change_owner(self, new_owner):
        self.owner = new_owner

    @classmethod
    def from_dict(cls, dict):
        name, age, species, owner = dict.values()
        return cls(name, age, species, owner)

    @classmethod
    def change_chirp(cls, new_chirp):
        cls.chirp = new_chirp

    @staticmethod
    def is_bird_adult(age):
        return age >= 3


bird1 = Bird.from_dict({"name": "Sunny", "age": 1, "species": "Canary", "owner": "Alice"})

# Виводимо інформацію про першу пташку
print(bird1)

bird1.chirp_sound()

Bird.change_chirp("Twee!")

bird1.chirp_sound()

print(Bird.is_bird_adult(5))

# Виводимо кількість створених пташок
print("Кількість ініціалізованих пташок: " + str(Bird.amount))
