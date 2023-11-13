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

class EmployeeManager:
    def __init__(self, employee_data): #ініціалізує менеджер із заданим EmployeeData екземпляром.
        self.employee_data = employee_data #Екземпляр класу EmployeeData, що представляє менеджер даних, працюватиме.

    def find_employee_by_number(self, number): #знаходить співробітника за його номером і повертає словник із відомостями про співробітника.
        if 1 <= number <= len(self.employee_data.names):
            index = number - 1
            employee = {
                "Name": self.employee_data.names[index],
                "Age": self.employee_data.ages[index],
                "Salary": self.employee_data.salaries[index],
                "Position": self.employee_data.positions[index],
                "Phone Number": self.employee_data.phone_numbers[index],
            }
            return employee
        else:
            return None

    def search_employees(self, criteria, value): #пошук співробітників на основі заданих критеріїв і цінностей. Повертає список відповідних індексів співробітників.
        matching_employees = []
        for i in range(len(self.employee_data.names)):
            if criteria == "Name" and value.lower() in self.employee_data.names[i].lower():
                matching_employees.append(i)
            elif criteria == "Age" and value == str(self.employee_data.ages[i]):
                matching_employees.append(i)
            elif criteria == "Salary" and value == str(self.employee_data.salaries[i]):
                matching_employees.append(i)
            elif criteria == "Position" and value.lower() in self.employee_data.positions[i].lower():
                matching_employees.append(i)
            elif criteria == "Phone Number" and value in self.employee_data.phone_numbers[i]:
                matching_employees.append(i)
        return matching_employees

class EmployeeInterface:
    def __init__(self, employee_data, employee_manager): # Ініціалізує інтерфейс екземплярами EmployeeDataта EmployeeManager.
        self.employee_data = employee_data #екземпляр класу EmployeeData.
        self.employee_manager = employee_manager #екземпляр класу EmployeeManager

    def run(self): #запускає основний цикл інтерфейсу користувача, дозволяючи користувачеві виконувати різні операції.
        while True:
            user_input = input(
                "Press 'q' to exit.\n"
                "Press 'a' to add a new employee.\n"
                "Press 'd' to delete an employee and enter their number.\n"
                "Press 'v' to view employee details.\n"
                "Press 'f' to find an employee by number.\n"
                "Press 's' to search employees by criteria.\n"
                "Press 't' to display the table.\n"
                "Press 'e' to edit an employee's details.\n"
            )

            if 't' in user_input.lower():
                self.display_table()
                continue_option = input("Press 'c' to continue or 'q' to exit: ")
                if continue_option.lower() == 'q':
                    self.employee_data.save_data()
                    break
                else:
                    continue

            if user_input.lower() == 'q':
                self.employee_data.save_data()
                break
            elif user_input.lower() == 'a':
                self.add_employee()
            elif user_input.lower() == 'd':
                self.delete_employee()
            elif user_input.lower() == 'v':
                self.view_employee()
            elif user_input.lower() == 'f':
                self.find_employee()
            elif user_input.lower() == 's':
                self.search_employees_menu()
            elif user_input.lower() == 'e':
                self.edit_employee()

    def display_table(self): #відображає таблицю даних про співробітників.
        print("| {:<5} | {:<20} | {:<5} | {:<10} | {:<25} | {:<15} |".format("No.", "Name", "Age", "Salary", "Position", "Phone Number"))
        print("-" * 99)
        for i in range(len(self.employee_data.names)):
            print("| {:<5} | {:<20} | {:<5} | ${:<9} | {:<25} | {:<15} |".format(i + 1, self.employee_data.names[i], self.employee_data.ages[i], self.employee_data.salaries[i], self.employee_data.positions[i], self.employee_data.phone_numbers[i]))
        print("-" * 99)

    def add_employee(self): #пропонує користувачеві ввести відомості про нового працівника та додає його до даних.
        new_name = input("Enter the name of the new employee: ")
        new_age = int(input("Enter the age of the new employee: "))
        new_salary_input = input("Enter the salary of the new employee: ")
        new_salary = int(new_salary_input.replace('$', ''))
        new_position = input("Enter the position of the new employee: ")
        new_phone_number = input("Enter the phone number of the new employee: ")
        self.employee_data.names.append(new_name)
        self.employee_data.ages.append(new_age)
        self.employee_data.salaries.append(new_salary)
        self.employee_data.positions.append(new_position)
        self.employee_data.phone_numbers.append(new_phone_number)
        print("Employee successfully added!")

    def delete_employee(self): #пропонує користувачеві ввести номер працівника, який потрібно видалити, і видаляє цього працівника з даних.
        try:
            delete_index = int(input("Enter the employee number you want to delete: ")) - 1
            if 0 <= delete_index < len(self.employee_data.names):
                del self.employee_data.names[delete_index]
                del self.employee_data.ages[delete_index]
                del self.employee_data.salaries[delete_index]
                del self.employee_data.positions[delete_index]
                del self.employee_data.phone_numbers[delete_index]
                print("Employee successfully deleted.")
            else:
                print("Invalid employee number.")
        except ValueError:
            print("Please enter an integer.")

    def view_employee(self): #пропонує користувачеві ввести номер працівника для перегляду та відображає деталі цього працівника.
        try:
            view_index = int(input("Enter the employee number you want to view: ")) - 1
            if 0 <= view_index < len(self.employee_data.names):
                print("\nEmployee Details:")
                print(f"Name: {self.employee_data.names[view_index]}")
                print(f"Age: {self.employee_data.ages[view_index]}")
                print(f"Salary: ${self.employee_data.salaries[view_index]}")
                print(f"Position: {self.employee_data.positions[view_index]}")
                print(f"Phone Number: {self.employee_data.phone_numbers[view_index]}\n")
            else:
                print("Invalid employee number.")
        except ValueError:
            print("Please enter an integer.")

    def find_employee(self): #пропонує користувачеві ввести номер працівника, якого потрібно знайти, і відображає деталі цього працівника.
        try:
            find_index = int(input("Enter the employee number you want to find: "))
            employee = self.employee_manager.find_employee_by_number(find_index)
            if employee:
                print("\nEmployee Details:")
                for key, value in employee.items():
                    print(f"{key}: {value}")
                print()
                continue_option = input("Press 'c' to continue: ")
                if continue_option.lower() != 'c':
                    return
            else:
                print("Invalid employee number.")
        except ValueError:
            print("Please enter an integer.")

    def search_employees_menu(self): #дозволяє користувачеві шукати співробітників на основі критеріїв і вартості.
        while True:
            criteria = input("Enter the search criteria (Name, Age, Salary, Position, Phone Number): ").strip()
            value = input(f"Enter the {criteria} to search for: ").strip()
            matching_indexes = self.employee_manager.search_employees(criteria, value)
            
            if matching_indexes:
                print("\nMatching Employees:")
                print("| {:<5} | {:<20} | {:<5} | {:<10} | {:<25} | {:<15} |".format("No.", "Name", "Age", "Salary", "Position", "Phone Number"))
                print("-" * 99)
                for index in matching_indexes:
                    print("| {:<5} | {:<20} | {:<5} | ${:<9} | {:<25} | {:<15} |".format(index + 1, self.employee_data.names[index], self.employee_data.ages[index], self.employee_data.salaries[index], self.employee_data.positions[index], self.employee_data.phone_numbers[index]))
                print("-" * 99)
                user_input = input("Press 'c' to continue, 'b' to go back, or 'q' to exit: ")
                
                if user_input.lower() == 'q':
                    return  # Exit the method and return to the main menu
                elif user_input.lower() == 'b':
                    return  # Exit the method and return to the main menu

            else:
                print("No matching employees found.")

    def edit_employee(self): #пропонує користувачеві ввести номер працівника для редагування та параметр для редагування, а потім оновлює відомості про працівника.
        try:
            edit_index = int(input("Enter the employee number you want to edit: ")) - 1
            if 0 <= edit_index < len(self.employee_data.names):
                print("\nEditing Employee Details:")
                print(f"1. Name: {self.employee_data.names[edit_index]}")
                print(f"2. Age: {self.employee_data.ages[edit_index]}")
                print(f"3. Salary: ${self.employee_data.salaries[edit_index]}")
                print(f"4. Position: {self.employee_data.positions[edit_index]}")
                print(f"5. Phone Number: {self.employee_data.phone_numbers[edit_index]}")
                edit_option = input("Enter the number of the parameter you want to edit: ")
                if edit_option == '1':
                    new_name = input("Enter the new name: ")
                    self.employee_data.names[edit_index] = new_name
                elif edit_option == '2':
                    new_age = int(input("Enter the new age: "))
                    self.employee_data.ages[edit_index] = new_age
                elif edit_option == '3':
                    new_salary_input = input("Enter the new salary: ")
                    new_salary = int(new_salary_input.replace('$', ''))
                    self.employee_data.salaries[edit_index] = new_salary
                elif edit_option == '4':
                    new_position = input("Enter the new position: ")
                    self.employee_data.positions[edit_index] = new_position
                elif edit_option == '5':
                    new_phone_number = input("Enter the new phone number: ")
                    self.employee_data.phone_numbers[edit_index] = new_phone_number
                print("Employee details successfully edited!")
            else:
                print("Invalid employee number.")
        except ValueError:
            print("Please enter an integer.")

if __name__ == "__main__": #Створює екземпляри EmployeeData, EmployeeManagerі EmployeeInterface.
    employee_data = EmployeeData()
    employee_data.load_data() #Виклики load_dataдля завантаження існуючих даних.
    employee_manager = EmployeeManager(employee_data)
    employee_interface = EmployeeInterface(employee_data, employee_manager)
    employee_interface.run() #Запускає основний цикл інтерфейсу користувача за допомогою run(). Якщо користувач вирішує вийти, він викликає save_dataзбереження даних перед виходом.



 
