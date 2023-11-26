# Зберігайте цей код у файлі main.py
from manager import StudentManager

if __name__ == "__main__":
    db_path = 'it-31-prach_nastya\\kursovaprachit-31\\students.db'
    manager = StudentManager(db_path)

    while True:
        print("Опції:")
        print("1. Вивести список студентів")
        print("2. Вивести успішність студентів")
        print("3. Додати студента")
        print("4. Видалити студента")
        print("5. Додати оцінку")
        print("6. Вийти")

        choice = input("Виберіть опцію: ")

        if choice == '1':
            manager.display_list()
        elif choice == '2':
            manager.display_grades()
        elif choice == '3':
            manager.add_entry()
        elif choice == '4':
            index = int(input("Введіть номер студента, якого потрібно видалити: ")) - 1
            manager.delete_entry(index)
        elif choice == '5':
            manager.add_grade()
        elif choice == '6':
            print("Дякуємо, що використовували нашу програму!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")
