# Зберігайте цей код у файлі interface.py
class UserInterface:
    @staticmethod
    def get_user_choice():
        """Отримує вибір користувача."""
        print("Опції:")
        print("1. Вивести список студентів")
        print("2. Вивести успішність студентів")
        print("3. Додати студента")
        print("4. Видалити студента")
        print("5. Додати оцінку")
        print("6. Вийти")
        return input("Виберіть опцію: ")

    @staticmethod
    def get_student_index():
        """Отримує індекс студента від користувача."""
        return int(input("Введіть номер студента: ")) - 1


