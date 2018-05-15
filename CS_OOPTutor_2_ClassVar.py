#Class Variables ......

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


#  INSTANCES OF THE CLASS
emp_1 = Employee('Evangelos', 'Germenis',50000)

emp_2 = Employee('Test', 'User', 60000)

#  NAME SPACE

# print(emp_1.__dict__) # Name space of instance / Doesn't contain raise_amount class var
# print(Employee.__dict__) # Name space of class /contains raise_amount class var

# Change Class variable / Changes for the instance too

# Employee.raise_amount = 1.05
#
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# /// CLASS VARIABLE USING "SELF"///  Set the raise amount var using an instance instead of a class

emp_1.raise_amount =1.05

print(emp_1.__dict__) # Employee 1 has the raise_amount var within it's name space now / found in it's own name space
                      # before going  and searching the class

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount) # We didn't set this raise_amount var for employee 2 , so that still falls back to the
                          # calsse's varaible value.


# /// CLASS VARIABLE WITH NO USE OF "SELF"// eg. keep track of number of employees

print(Employee.num_of_emps) # num_of_emps --> explained inside the class