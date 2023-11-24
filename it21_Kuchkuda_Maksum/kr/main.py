from employee_data import EmployeeData
from employee_manager import EmployeeManager
from employee_interface import EmployeeInterface



if __name__ == "__main__": #Створює екземпляри EmployeeData, EmployeeManagerі EmployeeInterface.
    employee_data = EmployeeData()
    employee_data.load_data() #Виклики load_data для завантаження існуючих даних.
    employee_manager = EmployeeManager(employee_data)
    employee_interface = EmployeeInterface(employee_data, employee_manager)
    employee_interface.run() #Запускає основний цикл інтерфейсу користувача за допомогою run(). Якщо користувач вирішує вийти, він викликає save_dataзбереження даних перед виходом.



 