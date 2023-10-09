# Підсистема 1
class Subsystem1:
    def start_engine(self):
        return "Запуск двигуна"

    def accelerate(self):
        return "Прискорення автомобіля"


# Підсистема 2
class Subsystem2:
    def activate_brakes(self):
        return "Активація гальм"

    def stop_engine(self):
        return "Зупинка двигуна"


# Фасад
class Facade:
    def __init__(self):
        self.subsystem1 = Subsystem1()
        self.subsystem2 = Subsystem2()

    def drive(self):
        actions = []
        actions.append(self.subsystem1.start_engine())
        actions.append(self.subsystem1.accelerate())
        actions.append(self.subsystem2.activate_brakes())
        actions.append(self.subsystem2.stop_engine())
        return "\n".join(actions)


# Використання фасаду для керування автомобілем
facade = Facade()
print(facade.drive())
