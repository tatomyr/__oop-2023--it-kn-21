class Bird:
    def __init__(self, name, age):
        self._name = None
        self._age = None
        self.name = name
        self.age = age

    def chirp(self):
        print("Chirp!")

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

bird = Bird("Tweety", 2)
bird.chirp()
print(bird.age)
bird.age = 3
print(bird.age)
bird.name = "Tweety Bird"
print(bird.name)
del bird.name
