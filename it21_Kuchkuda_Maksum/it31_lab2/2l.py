class Car:
    def __init__(self, make, model, year, engine_capacity, fuel_type):
        self.make = make
        self.model = model
        self.year = year
        self.engine_capacity = engine_capacity
        self.fuel_type = fuel_type

    def start(self):
        print(f"The {self.make} {self.model} has started.")

    def stop(self):
        print(f"The {self.make} {self.model} has stopped.")

    def display_info(self):
        print(f"Car: {self.make} {self.model} ({self.year})")
        print(f"Engine Capacity: {self.engine_capacity}L")
        print(f"Fuel Type: {self.fuel_type}")


# Приклад використання
my_car = Car(make="Toyota", model="Corolla", year=2020, engine_capacity=1.8, fuel_type="Petrol")

my_car.start()
my_car.display_info()
my_car.stop()