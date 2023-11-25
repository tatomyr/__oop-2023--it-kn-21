from hotel import Hotel

class HotelAdmin(Hotel):
    ADMIN_PASSWORD = '1233'  # Пароль адміністратора

    def authenticate_admin(self):
        password = input("Введіть пароль адміністратора: ")
        if password == self.ADMIN_PASSWORD:
            return True
        else:
            print("Неправильний пароль.")
            return False

    def register_room(self, room_number, capacity, amenities):
        if self.authenticate_admin():
            self.add_room(room_number, capacity, amenities)
            print(f"Номер {room_number} зареєстровано успішно.")
        else:
            print("Ви не маєте прав доступу для реєстрації номерів.")
