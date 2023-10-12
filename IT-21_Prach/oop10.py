from datetime import date

class Person:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate
        
    @property
    def age(self):
        today = date.today()
        age = today.year - self.birthdate.year
        if today < date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1
        return age
person = Person('John', date(1990, 1, 1))
print(person.age)  # 33
