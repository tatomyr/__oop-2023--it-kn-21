# Зберігайте цей код у файлі student.py
from prettytable import PrettyTable

class Student:
    def __init__(self, student_id, surname, name, group_name):
        self.student_id = student_id
        self.surname = surname
        self.name = name
        self.group_name = group_name
        self.grades = {}
