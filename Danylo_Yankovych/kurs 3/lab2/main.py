# Клас, що представляє інтерфейс для автомобілів.
class Car:
    def start(self):
        pass

    def stop(self):
        pass

# Клас, що представляє електричний автомобіль.
class ElectricCar(Car):
    def start(self):
        print("Електричний автомобіль запущений.")

    def stop(self):
        print("Електричний автомобіль зупинений.")

# Клас, що представляє двигун з бензиновим пальним.
class GasolineEngine:
    def ignite(self):
        print("Двигун з бензиновим пальним запущений.")

# Адаптер для автомобіля з бензиновим двигуном.
class GasolineCarAdapter(Car):
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        self.engine.ignite()

    def stop(self):
        print("Автомобіль з бензиновим двигуном зупинений.")

# Клієнтський код
electric_car = ElectricCar()
electric_car.start()
electric_car.stop()

gasoline_engine = GasolineEngine()
# gasoline_engine.start()  # Помилка, оскільки GasolineEngine не реалізує інтерфейс Car.

# Використання адаптера для автомобіля з бензиновим двигуном.
gasoline_car_adapter = GasolineCarAdapter(gasoline_engine)
gasoline_car_adapter.start()
gasoline_car_adapter.stop()
