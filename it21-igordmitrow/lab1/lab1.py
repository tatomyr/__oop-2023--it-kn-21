class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def set_age(self, age):
        self.age = age
    def __str__(self):
        return "Dog's name is " + self.name + ", age is " + str(self.age)
    def human_age(self):
        return self.age * 7
    
dog1 = Dog("Bob", 5)
print(dog1)