########## Породжувальний патерн - Фабрика #############

class Vehicle: 
    def __init__(self, model, state="доступний"):
        self.model = model
        self.state = state

    def display_info(self):
        return f"{self.model} - Стан: {self.state}"

class VehicleFactory:
    def create_vehicle(self, model, state = "доступний"):
        return Vehicle(model, state)
    
#############################################################    


########## Структурний патерн - Компонування #############

class VehicleRegistry:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def remove_vehicle(self, vehicle):
        self.vehicles.remove(vehicle)

    def display_all_vehicles(self):
        for vehicle in self.vehicles:
            print(vehicle.display_info())
    
    def filter_by_state(self, target_state):
        filtered_vehicles = [vehicle for vehicle in self.vehicles if vehicle.state == target_state]
        return filtered_vehicles
    
    def display_filtered_vehicles(self, target_state):
        filtered_vehicles = self.filter_by_state(target_state)
        for vehicle in filtered_vehicles:
            print(vehicle.display_info())

#############################################################


########## Поведінковий патерн - Команда #############
class ChangeStateCommand:
    def __init__(self, vehicle, new_state):
        self.vehicle = vehicle
        self.new_state = new_state

    def execute(self):
        self.vehicle.state = self.new_state

######################################################

# Створюємо транспортні засоби за допомогою фабричного методу
def main():
    fabric = VehicleFactory()
    registry = VehicleRegistry()

    registry.add_vehicle(fabric.create_vehicle("Авто №1", "зайнятий"))
    registry.add_vehicle(fabric.create_vehicle("Авто №2"))
    registry.add_vehicle(fabric.create_vehicle("Авто №3", "зайнятий"))
    registry.add_vehicle(fabric.create_vehicle("Вантажівка №1"))
    registry.add_vehicle(fabric.create_vehicle("Вантажівка №2", "зайнятий"))
    registry.add_vehicle(fabric.create_vehicle("Вантажівка №3"))
    registry.add_vehicle(fabric.create_vehicle("Мотоцикл №1"))

    while True:
        print("\n1. Додати новий вид транспортного засобу")
        print("2. Видалити транспортний засіб з реєстру")
        print("3. Змінити стан транспортного засобу")
        print("4. Вивести всі транспортні засоби в реєстрі")
        print("5. Фільтрувати транспортні засоби за станом")
        print("0. Вихід")

        choice = input("Введіть номер команди: ")

        if choice == "1":
            model = input("Введіть назву нового транспортного засобу: ")
            state = input("Введіть стан нового транспортного засобу: ")
            new_vehicle = fabric.create_vehicle(model, state)
            registry.add_vehicle(new_vehicle)
            print(f"Транспортний засіб {model} додано.")
        elif choice == "2":
            registry.display_all_vehicles()
            model = input("Введіть назву транспортного засобу для видалення з реєстру: ")
            for vehicle in registry.vehicles:
                if vehicle.model == model:
                    registry.remove_vehicle(vehicle)
                    print(f"Транспортний засіб {model} видалено з реєстру.")
                    break
            else:
                print(f"Транспортний засіб з назвою {model} не знайдено.")
        elif choice == "3":
            registry.display_all_vehicles()
            model = input("Введіть назву транспортного засобу, стан якого ви хочете змінити: ")
            for vehicle in registry.vehicles:
                if vehicle.model == model:
                    new_state = input("Введіть новий стан для транспортного засобу: ")
                    command = ChangeStateCommand(vehicle, new_state)
                    command.execute()
                    print(f"Стан транспортного засобу {model} змінено на {new_state}.")
                    break
            else:
                print(f"Транспортний засіб з назвою {model} не знайдено.")
        elif choice == "4":
            registry.display_all_vehicles()
        elif choice == "5":
            state_filter = input("Введіть стан для фільтрації транспортних засобів: ")
            print(f"\nФільтровані транспортні засоби за станом '{state_filter}':")
            registry.display_filtered_vehicles(state_filter)
        elif choice == "0":
            break
        else:
            print("Невідома команда. Спробуйте ще раз.")

main()

