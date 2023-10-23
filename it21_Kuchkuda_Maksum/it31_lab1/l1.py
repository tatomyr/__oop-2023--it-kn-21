import copy

class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"{self.color} {self.brand} {self.model}"

# Створення прототипу автомобіля
prototype_car = Car("Toyota", "Camry", "Silver")

# Клонування прототипу для створення нового автомобіля
new_car1 = prototype_car.clone()
new_car1.color = "Red"

new_car2 = prototype_car.clone()
new_car2.color = "Blue"

# Виведення інформації про автомобілі
print("Prototype Car:", prototype_car)
print("New Car 1:", new_car1)
print("New Car 2:", new_car2)
