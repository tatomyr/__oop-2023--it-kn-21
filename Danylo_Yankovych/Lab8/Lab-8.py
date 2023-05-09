class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
    
    def honk(self):
        print("Beep beep!")
    
    def __str__(self):
        return f"{self.color} {self.year} {self.make} {self.model}"

class SportsCar(Car):
    def __init__(self, make, model, year, color, top_speed):
        super().__init__(make, model, year, color)
        self.top_speed = top_speed
    
    def accelerate(self):
        print(f"The {self.color} {self.make} {self.model} is accelerating to {self.top_speed} mph!")
        
class ElectricCar(Car):
    def __init__(self, make, model, year, range, efficiency):
        super().__init__(make, model, year)
        self.range = range
        self.efficiency = efficiency
    
    def charge(self):
        print("Charging the electric car...")
    
    def drive(self, distance):
        energy = distance / self.efficiency
        if energy <= self.range:
            print(f"Driving the {self.make} {self.model} for {distance} km")
            self.range -= energy
        else:
            print(f"Oops, not enough energy to drive {distance} km")
    
    def __str__(self):
        return f"{self.make} {self.model} ({self.year}) - {self.range} km range, {self.efficiency} km/kWh efficiency"



dcar1 = Car("Honda", "Accord", 2022, "red")
print(car1) # red 2022 Honda Accord
car1.honk() # Beep beep!

car2 = SportsCar("Ferrari", "F8", 2021, "yellow", 211)
print(car2) # yellow 2021 Ferrari F8
car2.accelerate() # The yellow Ferrari F8 is accelerating to 211 mph!

car3 = ElectricCar("Tesla", "Model S", 2022, 500, 5)
print(car3)
car3.charge()
car3.drive(300)
print(car3)

print(isinstance(car2, ElectricCar)) # False
print(isinstance(car2, Car)) # True
print(isinstance(car2, SportsCar)) # True

print(issubclass(ElectricCar, Car)) # True
print(issubclass(ElectricCar, SportsCar)) # False
