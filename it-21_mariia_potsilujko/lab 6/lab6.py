class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.first = first + '.'+ last +'@company.com'

    def fullname(self):
       return '{} {}'.format(self.first, self.last)
        
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 90000)


emp_1.fullname()
print(Employee.fullname(emp_1))
