class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
person = Person("John Doe", 30)
person.name = "Jane Doe"
person.age = 35
person.display_info()  # виведе "Name: Jane Doe, Age: 35"
