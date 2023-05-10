class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        
    def description(self):
        return f"This is a {self.color} {self.year} {self.brand} {self.model} car."
car1 = Car('Ford', 'Mustang', 2020, 'red')
car2 = Car('Tesla', 'Model S', 2022, 'black')
print(car1.description())  # Виведе "This is a red 2020 Ford Mustang car."
print(car2.description())  # Виведе "This is a black 2022 Tesla Model S car."
