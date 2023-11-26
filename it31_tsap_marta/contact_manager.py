from databasemanager import DatabaseManager

from interface import ContactInterface

class ContactManager:
    def __init__(self):
        self.database_manager = DatabaseManager()
        self.interface = ContactInterface(self)

    def add_contact(self):
        name = input("Введіть ім'я контакту: ")
        phone = input("Введіть номер телефону контакту: ")
        email = input("Введіть email контакту: ")

        self.database_manager.add_contact(name, phone, email)
        
    def delete_contact(self):
        name = input("Введіть ім'я контакту, якого ви хочете видалити: ")
        self.database_manager.delete_contact(name)

    def edit_contact(self):
        name = input("Введіть ім'я контакту, якого ви хочете відредагувати: ")
        field = input("Введіть поле, яке ви хочете відредагувати (Телефон/Email): ").capitalize()
        new_value = input(f"Введіть нове значення для поля {field}: ")

        self.database_manager.edit_contact(name, field, new_value)

    def display_contacts(self):
        self.database_manager.display_contacts()

    def search_contact(self):
        name = input("Введіть ім'я контакту, якого ви шукаєте: ")
        self.database_manager.search_contact(name)

    def run(self):
        self.interface.run_interface()

