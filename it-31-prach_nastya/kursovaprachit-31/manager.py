# Зберігайте цей код у файлі manager.py
# Зберігайте цей код у файлі manager.py
from database import DatabaseManager
from input import StudentInput
from output import StudentOutput
from student import Student

class StudentManager:
    def __init__(self, db_path):
        self.db_manager = DatabaseManager(db_path)
        self.data = self.load_data()
        self.input_handler = StudentInput()
        self.output_handler = StudentOutput()

    def initialize_database(self):
        self.db_manager.initialize_database()

    def save_data(self):
        self.db_manager.save_data(self.data)

    def load_data(self):
        return self.db_manager.load_data()



    def display_list(self):
        """Виводить список студентів за допомогою відповідного об'єкта виводу."""
        self.output_handler.display_student_list(self.data)

    def display_grades(self):
        """Виводить оцінки для конкретного студента."""
        self.display_list()
        student_index = self.input_handler.get_student_index()

        if 0 <= student_index < len(self.data):
            student = self.data[student_index]
            self.output_handler.display_student_grades(student)
        else:
            print("Невірний номер студента.")

    def add_entry(self):
        """Додає нового студента до списку з перевіркою на дублікати та зберігає дані у базі даних."""
        entry = self.input_handler.get_student_entry()
        if entry.surname.strip() != '' and entry.name.strip() != '' and entry.group_name.strip() != '':
            if not self.db_manager.has_duplicate(entry.student_id, entry.surname, entry.name, entry.group_name):
                self.data.append(entry)
                self.save_data()
                print("Студента додано.")
            else:
                print("Такий студент вже існує.")
        else:
            print("Порожні дані не додаватимуться.")

    def delete_entry(self, index):
        """Видаляє студента зі списку за індексом та оновлює дані у базі даних."""
        if 0 <= index < len(self.data):
            self.data.pop(index)
            self.save_data()  # Оновлюємо дані у базі даних
            print("Студента видалено.")
        else:
            print("Невірний номер студента.")

    def add_grade(self):
        """Додає оцінку для конкретного студента."""
        self.display_list()  # Покаже список студентів для вибору
        student_index = self.input_handler.get_student_index()

        if 0 <= student_index < len(self.data):
            student = self.data[student_index]
            subject = input("Введіть предмет: ")
            grade = int(input("Введіть оцінку: "))
            
            student.grades[subject] = grade
            self.save_data()  # Зберігаємо дані у базі даних
            print(f"Оцінка {grade} для предмета {subject} додана для студента {student.surname} {student.name}.")
        else:
            print("Невірний номер студента.")
