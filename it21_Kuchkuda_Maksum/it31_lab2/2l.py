class Car:
    def __init__(self):
        self.make = None
        self.model = None
        self.color = None

    def __str__(self):
        return f"Car: {self.make}, Model: {self.model}, Color: {self.color}"


class CarBuilder:
    def __init__(self, make, model):
        self.car = Car()
        self.car.make = make
        self.car.model = model

    def set_color(self, color):
        self.car.color = color

    def build(self):
        return self.car

car_builder = CarBuilder("Toyota", "Corolla")
car_builder.set_color("Blue")
car = car_builder.build()

print(car)  
