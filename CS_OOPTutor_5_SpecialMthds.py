# Dunders /operator overloading
# Denpends on what type of object you working,operations work different


class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
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


# //// SPECIAL METHODS Dunder repr /str etc///
# Make sure you at least have an repr method, because if we have reprs without str(frontend) then calling an str
# on an employee we ll just use the repr as a fallback

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

# str method : Enduser

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

# Dunder add method / customize addition ...add employees by its salaries

    def __add__(self, other):
        return self.pay + other.pay

# Dunder len method / (return the total num of chars in their fullname )

    def __len__(self):
        return len(self.fullname())


# INSTANCES OF THE CLASS
emp_1 = Employee('Evangelos', 'Germenis',50000)
emp_2 = Employee('Test', 'User', 60000)


# print(emp_1) # Returns the string that we specified in repr method or str first if it is defined

print(repr(emp_1))
print(str(emp_1))

# ///// Explicitly specify dunder methods////////

print(emp_1.__repr__())
print(emp_1.__str__())

# ///// Dunder add method use (add salaries) //////
# (specify with a method how to add an employee object)

print(emp_1 + emp_2)

# ///// Dunder len method use //////
# (return the total num of chars in their fullname )

print(len(emp_1))