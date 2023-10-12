class Transport:
    def __init__(self, speed):
        self.speed = speed
    
    def go(self):
        print("Транспорт рухається зі швидкістю", self.speed)

class Car(Transport):
    def __init__(self, speed, doors):
        super().__init__(speed)
        self.doors = doors
    
    def go(self):
        super().go()
        print("Автомобіль їде з відкритими вікнами та зі швидкістю", self.speed)
    
    def get_doors(self):
        return self.doors

class Airplane(Transport):
    def __init__(self, speed, altitude):
        super().__init__(speed)
        self.altitude = altitude
    
    def go(self):
        super().go()
        print("Літак летить на висоті", self.altitude)
    
    def get_altitude(self):
        return self.altitude

car = Car(60, 4)
car.go()
print("Кількість дверей:", car.get_doors())

airplane = Airplane(800, 10000)
airplane.go()
print("Висота польоту:", airplane.get_altitude())
