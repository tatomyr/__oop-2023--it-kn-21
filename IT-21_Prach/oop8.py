class Vehicle:
    def __init__(self, wheels, max_speed):
        self.wheels = wheels
        self.max_speed = max_speed

class Car(Vehicle):
    def __init__(self, wheels, max_speed, make, model, color):
        super().__init__(wheels, max_speed)
        self.make = make
        self.model = model
        self.color = color
car = Car(4, 200, "Tesla", "Model S", "red")
print(car.wheels) # виведе 4
print(car.max_speed) # виведе 200
print(car.make) # виведе "Tesla"
print(car.model) # виведе "Model S"
print(car.color) # виведе "red"
