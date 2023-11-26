from abc import ABC, abstractmethod

# Абстрактні класи для виробів
class Transport(ABC):
    @abstractmethod
    def transport(self):
        pass

class Car(Transport):
    def transport(self):
        return "Автомобіль перевозить пасажирів"

class Plane(Transport):
    def transport(self):
        return "Літак перевозить пасажирів по повітрю"

# Абстрактна фабрика
class TransportFactory(ABC):
    @abstractmethod
    def create_transport(self) -> Transport:
        pass

# Конкретні Фабрики для видів транспорту
class CarFactory(TransportFactory):
    def create_transport(self) -> Transport:
        return Car()

class PlaneFactory(TransportFactory):
    def create_transport(self) -> Transport:
        return Plane()

# Клієнтський
def use_factory(factory: TransportFactory):
    transport = factory.create_transport()
    print(transport.transport())

# Використання фабрик для створення транспорту
car_factory = CarFactory()
use_factory(car_factory)

plane_factory = PlaneFactory()
use_factory(plane_factory)





