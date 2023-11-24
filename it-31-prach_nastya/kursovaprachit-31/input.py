# Зберігайте цей код у файлі input.py
from student import Student

class StudentInput:
    @staticmethod
    def get_student_entry():
        student_id = int(input("Введіть номер студента: "))
        surname = input("Введіть прізвище: ")
        name = input("Введіть ім'я: ")
        group_name = input("Введіть назву групи: ")
        return Student(student_id, surname, name, group_name)

    @staticmethod
    def get_student_index():
        return int(input("Введіть номер студента: ")) - 1
