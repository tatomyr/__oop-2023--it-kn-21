class ContactInterface:
    def __init__(self, contact_manager):
        self.contact_manager = contact_manager

    def run_interface(self):
        while True:
            print("\nМенеджер контактів")
            print("1. Додати контакт")
            print("2. Видалити контакт")
            print("3. Редагувати контакт")
            print("4. Показати всі контакти")
            print("5. Пошук контакту за ім'ям")
            print("6. Вийти")

            choice = input("Виберіть опцію (1/2/3/4/5/6): ")

            if choice == '1':
                self.contact_manager.add_contact()
            elif choice == '2':
                self.contact_manager.delete_contact()
            elif choice == '3':
                self.contact_manager.edit_contact()
            elif choice == '4':
                self.contact_manager.display_contacts()
            elif choice == '5':
                self.contact_manager.search_contact()
            elif choice == '6':
                print("Дякую за використання Менеджера контактів. До побачення!")
                break
            else:
                print("Невірний вибір. Будь ласка, виберіть існуючу опцію (1/2/3/4/5/6).")
