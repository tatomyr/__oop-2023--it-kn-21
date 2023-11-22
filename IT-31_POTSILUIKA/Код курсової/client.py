from hotel import Hotel

class HotelClient(Hotel):
    def book_room(self, room_number, date):
        if room_number in self.check_availability(date):
            super().book_room(room_number, date)
        else:
            print("Цей номер вже заброньовано або не існує.")

    def view_available_rooms(self, date):
        available_rooms = self.check_availability(date)
        print(f"Вільні номери на {date}: {available_rooms}")
