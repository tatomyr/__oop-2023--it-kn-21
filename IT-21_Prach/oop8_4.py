class Vehicle:
    pass

class Car(Vehicle):
    pass

class Truck(Vehicle):
    pass

print(issubclass(Car, Vehicle)) # True
print(issubclass(Truck, Vehicle)) # True
print(issubclass(Car, Truck)) # False
print(issubclass(Truck, Car)) # False
