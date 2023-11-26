import sqlite3
from manager import Contact

 
class DatabaseManager:
    def __init__(self, db_file="contacts.db"):
        self.conn = sqlite3.connect(db_file)
        self.create_table()
        self.load_data()

    def create_table(self):
        c = self.conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS contacts (
                         name text,
                         phone text,
                         email text
                 )""")
        self.conn.commit()

    def load_data(self):
        c = self.conn.cursor()
        c.execute("SELECT * FROM contacts")
        data = c.fetchall()
        self.contacts = {entry[0]: Contact(entry[0], entry[1], entry[2]) for entry in data}

    def save_data(self):
        c = self.conn.cursor()
        c.execute("DELETE FROM contacts")
        data = [(name, contact.phone, contact.email) for name, contact in self.contacts.items()]
        c.executemany("INSERT INTO contacts VALUES (?, ?, ?)", data)
        self.conn.commit()

    def add_contact(self, name, phone, email):
        if name in self.contacts:
            print(f"Контакт з ім'ям {name} вже існує. Виберіть інше ім'я.")
        else:
            contact = Contact(name, phone, email)
            self.contacts[name] = contact
            self.save_data()
            print(f"Контакт {name} доданий.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            self.save_data()
            print(f"Контакт {name} видалений.")
        else:
            print(f"Контакт {name} не існує в базі даних.") 

    def edit_contact(self, name, field, new_value):
        if name in self.contacts:
            contact = self.contacts[name]
            if field == 'Телефон':
                contact.set_phone(new_value)
            elif field == 'Email':
                contact.set_email(new_value)
            self.save_data()
            print(f"{field} для контакту {name} змінено на {new_value}.")
        else:
            print(f"Контакт {name} не існує в базі даних.")

    def display_contacts(self):
        if not self.contacts:
            print("Список контактів порожній.")
        else:
            print("Список контактів:")
            for name, contact in self.contacts.items():
                print(contact)
                print()

    def search_contact(self, name):
        if name in self.contacts:
            contact = self.contacts[name]
            print(f"Знайдено контакт для {name}:")
            print(contact)
        else:
            print(f"Контакт {name} не знайдено.")
            






