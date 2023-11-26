class EmployeeData:
    def __init__(self): #Ініціалізує порожні списки для атрибутів.
        self.names = [] #список для збереження імен співробітників.
        self.ages = [] #список для збереження віку співробітників.
        self.salaries = [] #список для зберігання зарплат співробітників.
        self.positions = [] #список для збереження посад співробітників.
        self.phone_numbers = [] #cписок для збереження номерів телефонів співробітників.

    def load_data(self): #завантажує дані з файлу ("list.txt") у списки. Якщо файл не знайдено, він друкує повідомлення та починає з порожніми даними.
        try:
            with open("list.txt", "r") as file:
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) == 5:
                        name, age, salary, position, phone_number = parts
                        self.names.append(name)
                        self.ages.append(int(age))
                        self.salaries.append(int(salary.replace('$', '')))
                        self.positions.append(position)
                        self.phone_numbers.append(phone_number)
                    else:
                        print("Invalid data format in the file.")
        except FileNotFoundError:
            print("File not found. Starting with empty data.")

    def save_data(self): #Зберігає поточні дані зі списків у файл ("list.txt").
        with open("list.txt", "w") as file:
            for i in range(len(self.names)):
                file.write(f"{self.names[i]},{self.ages[i]},{self.salaries[i]},{self.positions[i]},{self.phone_numbers[i]}\n")
