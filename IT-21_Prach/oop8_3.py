class Vehicle:
    pass

class Car(Vehicle):
    pass

class Truck(Vehicle):
    pass

car = Car()
truck = Truck()

print(isinstance(car, Vehicle)) # True
print(isinstance(truck, Vehicle)) # True
print(isinstance(car, Truck)) # False
print(isinstance(truck, Car)) # False
