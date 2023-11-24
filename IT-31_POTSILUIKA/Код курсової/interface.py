from admin import HotelAdmin
from client import HotelClient

def run_interface():
    admin = HotelAdmin()
    client = HotelClient()

    while True:
        print("Ласкаво просимо до системи готелю!")
        print("1. Переглянути вільні номери")
        print("2. Зареєструвати новий номер (тільки для адміністратора)")
        print("3. Забронювати номер")
        print("4. Вийти")

        choice = input("Виберіть опцію: ")

        if choice == '1':
            date = input("Введіть дату для перевірки доступних номерів (формат: РРРР-ММ-ДД): ")
            client.view_available_rooms(date)
        elif choice == '2':
            admin.register_room(input("Введіть номер кімнати: "), int(input("Введіть кількість місць: ")), input("Введіть зручності: "))
        elif choice == '3':
            date = input("Введіть дату для бронювання (формат: РРРР-ММ-ДД): ")
            client.view_available_rooms(date)
            room_number = input("Введіть номер кімнати для бронювання: ")
            client.book_room(room_number, date)
        elif choice == '4':
            admin.close_connection()
            client.close_connection()
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Будь ласка, спробуйте ще раз.")

if __name__ == "__main__":
    run_interface()
