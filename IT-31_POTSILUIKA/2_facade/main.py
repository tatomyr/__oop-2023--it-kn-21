# Підсистема для управління резерваціями
class ReservationSystem:
    def make_reservation(self, guest_name, room_number):
        print(f"Створено резервацію для {guest_name} в номері {room_number}")

    def cancel_reservation(self, guest_name, room_number):
        print(f"Скасовано резервацію для {guest_name} в номері {room_number}")

# Підсистема для обліку постояльців
class GuestManagementSystem:
    def check_in(self, guest_name, room_number):
        print(f"{guest_name} заселяється в номер {room_number}")

    def check_out(self, guest_name, room_number):
        print(f"{guest_name} виселяється з номера {room_number}")

# Фасад для автоматизованої системи обліку готелю
class HotelFacade:
    def __init__(self):
        self.reservation_system = ReservationSystem()
        self.guest_management_system = GuestManagementSystem()

    def book_room(self, guest_name, room_number):
        self.reservation_system.make_reservation(guest_name, room_number)
        self.guest_management_system.check_in(guest_name, room_number)

    def cancel_reservation(self, guest_name, room_number):
        self.reservation_system.cancel_reservation(guest_name, room_number)
        self.guest_management_system.check_out(guest_name, room_number)

# Використання патерну Фасад
if __name__ == "__main__":
    hotel_facade = HotelFacade()

    # Бронювання номеру
    guest_name = "John"
    room_number = 101
    hotel_facade.book_room(guest_name, room_number)

    # Скасування резервації та виселення
    hotel_facade.cancel_reservation(guest_name, room_number)