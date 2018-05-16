#Sub -Classing

class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

        Employee.num_of_emps += 1 # We do the count inside the __init__ method since the init method runs everytime we
                                  # create a new employees

    #  METHOD OF THE CLASS
    def fullname(self):
        return '{} {}'.format(self.first, self.last) # return full name in a format /dynamic


    def aplly_raise(self):
        self.pay = int(self.pay * self.raise_amount) # The self.raise_amount will give us the ability to change
                                                     # that amount for a single instance

#  //////SUB-CLASS -INHERITANCE ///////

class Developer(Employee):

    raise_amount = 1.10 #Doesn't affect our parent class variables/print Employee again

    def __init__(self, first, last, pay, prog_lang):
        Employee.__init__(self,first, last, pay) ## Same like super. but better used when we handle multiple inheritance
        # super().__init__(first, last, pay) # NOT WORKING IN 2.7 Python!!!
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees = None):
        Employee.__init__(self,first, last, pay) ## Same like super. but better used when we handle multiple inheritance

        if employees is None:
            self.employees = [] # empty list
        else:
            self.employees = employees

    def add_employee(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self,emp):
        if emp in self.employees :
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())






dev_1 = Developer('Evangelos', 'Germenis', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

# ////// VARIABLE CHECK WITH PARENT CLASS /////
# print(dev_1.pay)
# dev_1.aplly_raise()
# print(dev_1.pay)

# ////// SUB class Developer customize /////

# print(dev_1.email)
# print(dev_1.prog_lang)

# ////// SUB Class Manager Methods /////

print(mgr_1.email)
mgr_1.add_employee(dev_2) # Add employee
mgr_1.remove_employee(dev_1) # Remove employee
mgr_1.print_emps()

# //// isinstance / isclass /////

print(isinstance(mgr_1, Manager))

print(isinstance(mgr_1, Employee))

print(isinstance(mgr_1, Developer)) # Retruns false / Even though developer and manager both inherit from Employee they aren't
                                    #part of it's own inheritance

print(issubclass(Developer, Employee)) # True
print(issubclass(Manager, Employee))  # True
print(issubclass(Manager, Developer)) # False
