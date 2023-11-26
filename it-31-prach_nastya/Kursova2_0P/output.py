# Зберігайте цей код у файлі output.py

from prettytable import PrettyTable

class StudentOutput:
    @staticmethod
    def display_student_list(data):
        """Виводить список студентів у вигляді таблиці."""
        table = PrettyTable()
        table.field_names = ["#", "ID", "Прізвище", "Ім'я", "Група"]

        for idx, student in enumerate(data, start=1):
            table.add_row([idx, student.student_id, student.surname, student.name, student.group_name])

        print(table)

    @staticmethod
    def display_student_grades(student):
        """Виводить оцінки для конкретного студента."""
        table = PrettyTable()
        table.field_names = ["Предмет", "Оцінка"]

        for subject, grade in student.grades.items():
            table.add_row([subject, grade])

        print(f"Успішність студента {student.surname} {student.name}:")
        print(table)
