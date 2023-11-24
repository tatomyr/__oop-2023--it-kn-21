# Зберігайте цей код у файлі database.py
import sqlite3
from student import Student

class DatabaseManager:
    def __init__(self, db_path):
        self.db_path = db_path
        self.initialize_database()
        self.data = self.load_data()

    def initialize_database(self):
        """Ініціалізує базу даних та створює таблицю, якщо її ще не існує."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS students (
                    student_id INTEGER PRIMARY KEY,
                    surname TEXT NOT NULL,
                    name TEXT NOT NULL,
                    group_name TEXT NOT NULL
                )
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS grades (
                    student_id INTEGER,
                    subject TEXT NOT NULL,
                    grade INTEGER,
                    FOREIGN KEY (student_id) REFERENCES students (student_id)
                )
            """)
            conn.commit()

    def load_data(self):
        """Завантажує дані з бази даних у список об'єктів Student."""
        data = []
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT student_id, surname, name, group_name FROM students")
            rows = cursor.fetchall()
            for row in rows:
                student_id, surname, name, group_name = row
                student = Student(student_id, surname, name, group_name)
                # Завантаження оцінок для кожного студента
                cursor.execute("SELECT subject, grade FROM grades WHERE student_id = ?", (student_id,))
                grades = cursor.fetchall()
                for subject, grade in grades:
                    student.grades[subject] = grade
                data.append(student)
        return data

    def save_data(self, data):
        """Зберігає дані зі списку у базі даних."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM students")
            cursor.execute("DELETE FROM grades")
            for student in data:
                cursor.execute("INSERT INTO students (student_id, surname, name, group_name) VALUES (?, ?, ?, ?)",
                               (student.student_id, student.surname, student.name, student.group_name))
                for subject, grade in student.grades.items():
                    cursor.execute("INSERT INTO grades (student_id, subject, grade) VALUES (?, ?, ?)",
                                   (student.student_id, subject, grade))
            conn.commit()

    def has_duplicate(self, student_id, surname, name, group_name):
        """Перевіряє, чи існує дублікат студента в базі даних."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT COUNT(*) FROM students WHERE student_id = ? OR (surname = ? AND name = ? AND group_name = ?)",
                               (student_id, surname, name, group_name))
                count = cursor.fetchone()[0]
                return count > 0
        except sqlite3.Error as e:
            print(f"Помилка перевірки дублікатів: {e}")
            return False
