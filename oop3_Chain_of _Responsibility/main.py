# Клас для представлення готельного номеру
class HotelRoom:
    def __init__(self, room_number):
        self.room_number = room_number
        self.is_occupied = False

    def check_in(self, guest_name):
        if not self.is_occupied:
            self.is_occupied = True
            print(f"{guest_name} заселяється в номер {self.room_number}")
        else:
            print(f"Номер {self.room_number} вже зайнятий")

    def check_out(self, guest_name):
        self.is_occupied = False
        print(f"{guest_name} виселяється з номера {self.room_number}")

# Базовий клас обробника запитів
class Handler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle_request(self, guest_name, room_number):
        if self.successor:
            self.successor.handle_request(guest_name, room_number)

# Обробник запиту для заселення в стандартний номер
class StandardRoomHandler(Handler):
    def handle_request(self, guest_name, room_number):
        if room_number % 2 == 0:  # Якщо номер парний, то це стандартний номер
            room = HotelRoom(room_number)
            room.check_in(guest_name)
        elif self.successor:
            self.successor.handle_request(guest_name, room_number)

# Обробник запиту для заселення в номер "люкс"
class DeluxeRoomHandler(Handler):
    def handle_request(self, guest_name, room_number):
        if room_number % 2 == 1:  # Якщо номер непарний, то це номер "люкс"
            room = HotelRoom(room_number)
            room.check_in(guest_name)
        elif self.successor:
            self.successor.handle_request(guest_name, room_number)

# Використання паттерну "Chain of Responsibility"
if __name__ == "__main__":
    # Створення ланцюга обробників
    standard_handler = StandardRoomHandler()
    deluxe_handler = DeluxeRoomHandler(standard_handler)

    # Заселення гостей у різні номери
    guest1 = "John"
    guest2 = "Alice"
    guest3 = "Bob"

    deluxe_handler.handle_request(guest1, 101)
    deluxe_handler.handle_request(guest2, 102)
    deluxe_handler.handle_request(guest3, 103)
    deluxe_handler.handle_request(guest1, 104)
