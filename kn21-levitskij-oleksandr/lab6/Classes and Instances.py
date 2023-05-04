class Employee:

    def __init__(self, first, last, pay):
        self.first = first 
        self.last = last 
        self.pay = pay 
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(emp_1.first, emp_1.last) 
    def namepay(self):
        return '{} {}'.format(emp_1.first, emp_1.pay)
    

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

emp_1.fullname()
emp_1.namepay()
print(Employee.fullname(emp_1))
print(Employee.namepay(emp_1))
print(emp_1.email)
print(emp_1.pay)
#print('{} {}'.format(emp_1.first, emp_1.last))