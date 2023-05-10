import datetime

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.birthdate = datetime.date.today() - datetime.timedelta(days=age*365)
    
    @classmethod
    def from_birthdate(cls, name, birthdate):
        age = (datetime.date.today() - birthdate).days // 365
        return cls(name, age)
birthdate = datetime.date(1990, 5, 9)
p = Person.from_birthdate("Mike", birthdate)
print(p.name)  # виведе "Mike"
print(p.age)  # виведе 31
print(p.birthdate)  # виведе дату народження, наприклад "1990-05-09"
