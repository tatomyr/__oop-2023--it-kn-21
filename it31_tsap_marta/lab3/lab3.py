# Клас для стану
class State:
    def switch(self):
        pass

# Конкретні стани
class OnState(State):
    def switch(self):
        print("Світло вже увімкнено.")

class OffState(State):
    def switch(self):
        print("Увімкнути світло.")
        return OnState()

class EmergencyState(State):
    def switch(self):
        print("В аварійному стані. Вимкнути світло.")
        return OffState()

# Клас для пристрою керування світлом
class LightSwitch:
    def __init__(self):
        self.state = OffState()

    def switch(self):
        self.state = self.state.switch()

# Приклад використання
light_switch = LightSwitch()

light_switch.switch()  # Увімкнути світло.
light_switch.switch()  # Світло вже увімкнено.
light_switch.switch()  # В аварійному стані. Вимкнути світло.
light_switch.switch()  # Увімкнути світло.
