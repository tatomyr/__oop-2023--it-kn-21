class Car:
    # змінна класу
    num_wheels = 4
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = 0
    
    def drive(self, miles):
        self.mileage += miles
    
    def __str__(self):
        return f"{self.year} {self.make} {self.model}, mileage: {self.mileage}"
print(Car.num_wheels)  # виведе 4

my_car = Car('Toyota', 'Corolla', 2022)
print(my_car.num_wheels)  # виведе 4

Car.num_wheels = 3
print(Car.num_wheels)  # виведе 3
print(my_car.num_wheels)  # виведе 3, тому що змінна класу була змінена

her_car = Car('Honda', 'Accord', 2021)
print(her_car.num_wheels)  # виведе 3, тому що змінна класу має тепер значення 3
