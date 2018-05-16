# Decorators ,  Getters, Setters and Deleters


class Employee(object):

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last):
        self.first = first
        self.last = last

    #  METHOD OF THE CLASS

    # In order to continue access email as an attribute i have to add a property decorator

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last) # return full name in a format /dynamic

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # Setter /Deleter ....This don't apply with old style class ..new style class Employee(object)
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    #
    #Deleter /Clean -up code Python 3
    @fullname.deleter
    def fullname(self):
        print('Delete name')
        self.first = None
        self.last = None

emp_1 = Employee('John', 'Smith')

# Try to change the email also
# emp_1.first = 'Jim'

# Setter [Try to change first and last name]
emp_1.fullname = 'Corey Schafer'

print(emp_1.first)

# print(emp_1.email()) # you have to change the code everywhere / access the email like a method

print(emp_1.email) # Adding the property decorator now you can access the email like an attribute
                   # we are defining the email in our class like it is a method but we are accessing it like it was an attribute

print(emp_1.fullname)

del emp_1.fullname # # Applies only with new style class definition