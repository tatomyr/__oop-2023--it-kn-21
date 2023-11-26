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
