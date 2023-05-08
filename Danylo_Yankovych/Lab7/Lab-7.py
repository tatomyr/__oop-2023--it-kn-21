class Dog:
    amount = 0
    woof = "Woof!"

    def __init__(self, name, age, breed, owner):
        self.name = name
        self.age = age
        self.breed = breed
        self.owner = owner
        Dog.amount += 1

    def __str__(self):
        return f"{self.name} is {self.age} years old, {self.breed} breed, owner is {self.owner}"

    def bark(self):
        print(self.name + ": " + self.woof)

    def get_older(self):
        self.age += 1

    def get_age(self):
        return self.age

    def change_owner(self, new_owner):
        self.owner = new_owner

    @classmethod
    def from_dict(cls, dict):
        name, age, breed, owner = dict.values()
        return cls(name, age, breed, owner)

    @classmethod
    def change_woof(cls, new_woof):
        cls.woof = new_woof

    @staticmethod
    def is_dog_adult(age):
        return age >= 3


dog1 = Dog.from_dict({"name": "Boxer", "age": 2, "breed": "Bulldog", "owner": "Danylo"})

print(dog1)

dog1.bark()

Dog.change_woof("Aw-aw!")

dog1.bark()

print(Dog.is_dog_adult(5))

print("ʳ������ �������������� �����: " + str(Dog.amount))