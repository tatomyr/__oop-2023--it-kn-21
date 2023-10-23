class Dog:

    amount = 0
    woof = "Woof!"

    def __init__(self, name, age, breed, owner) -> None:
        self.name = name
        self.age = age
        self.breed = breed
        self.owner = owner
        Dog.amount += 1

    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old, {self.breed} breed, owner is {self.owner}"
    
    def bark(self):
        print(self.woof)
    
    def get_older(self):
        self.age += 1

    def get_age(self):
        return self.age
    
    def change_owner(self, new_owner):
        self.owner = new_owner

dog1 = Dog("Rex", 3, "Labrador", "Kurac")
dog2 = Dog("Bob", 5, "Pitbull", "Kurac")
dog3 = Dog("Jack", 2, "Poodle", "Kurac")

# Bob is barking
dog2.bark()

# Displaying fisrt dog's age incrementing it by 1 year
print(dog3.get_age())
dog3.get_older()
print(dog3.get_age())

# Changing the fist dog's owner
dog1.change_owner("Lionel Messi")

# Displaying info about first dog
print(dog1)

# Displaying the number of created dogs
print("Amount of instantiated dogs " + str(Dog.amount))
