class Employee:
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first 
        self.last = last 
        self.pay = pay 
        self.email = first + '.' + last + '@company.com'
        
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last) 
    
    def namepay(self):
        return '{} {}'.format(self.first, self.pay)
    
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)
print(Employee.fullname(emp_1))
print(Employee.namepay(emp_1))
print(emp_1.email)
print(emp_1.pay)
#print('{} {}'.format(emp_1.first, emp_1.last))
print(Employee.num_of_emps)