#  Python OOP Reg, Stat , Cls methods

class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay ):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

        Employee.num_of_emps += 1 # We do the count inside the __init__ method since the init method runs everytime we
                                  # create a new employe

    #  METHOD OF THE CLASS
    def fullname(self):
        return '{} {}'.format(self.first, self.last) # return full name in a format /dynamic


    def aplly_raise(self):
        self.pay = int(self.pay * self.raise_amount) # The self.raise_amount will give us the ability to change
                                                     # that amount for a single instance

    # ///CLASS METHOD ///

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod # // Alternative Constructor
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-') # Split the string and
        return cls(first, last, pay) # create the object employee

    # ///STATIC METHOD ///

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


#  INSTANCES OF THE CLASS
emp_1 = Employee('Evangelos', 'Germenis',50000)
emp_2 = Employee('Test', 'User', 60000)

Employee.set_raise_amount(1.05) # Call the class method and change the class variable


print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# //// NEW Example  ////

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

#  1st method - solution
# first, last, pay = emp_str_1.split('-')
# new_emp_1 = Employee(first, last, pay)


#  2nd method - solution
# We need to create an alternative constructor that allows to pass the string and create an employee object

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)

#/// STATIC METHOD EXAMPLE /// recieve date and check if it's a working day

import datetime

my_date = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date))