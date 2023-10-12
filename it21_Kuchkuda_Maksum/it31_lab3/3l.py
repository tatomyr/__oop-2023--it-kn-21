class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

# Створення класу, який представляє список автомобілів
class CarList:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def iterate_cars(self):
        for car in self.cars:
            yield car

# Створення об'єктів автомобілів
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")
car3 = Car("Ford", "Focus")

# Створення колекції автомобілів
car_list = CarList()
car_list.add_car(car1)
car_list.add_car(car2)
car_list.add_car(car3)

# Використання ітератора для виведення автомобілів
print("List of cars:")
for car in car_list.iterate_cars():
    print(f"Brand: {car.brand}, Model: {car.model}")