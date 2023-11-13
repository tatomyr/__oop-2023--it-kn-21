class Employee:

    num_of_emps = 0
    raise_emount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay

        Employee.num_of_emps += 1 
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
        
    def appy_raise(self):
        self.pay = int(self.pay * self.raise_emount)

    @classmethod
    def set_raise_amt(cls, amout):
        cls.raise_emount = amout
    
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee('Corney', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

import datetime
my_date = datetime.date(2016, 7, 10)


emp_1.appy_raise()
emp_2.appy_raise()

emp_str = "John-Doe-70000"
emp_3 = Employee.from_string(emp_str)
print(emp_3.first)  # Output: John
print(emp_3.last)   # Output: Doe
print(emp_3.pay)    # Output: 70000

print(emp_1.pay)  
print(emp_2.pay)

print(Employee.is_workday(my_date))
