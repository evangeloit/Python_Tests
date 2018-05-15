# CLasses


class Employee:

    def __init__(self, first, last, pay ):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

    #  METHOD OF THE CLASS
    def fullname(self):
        return '{} {}'.format(self.first, self.last) # return full name in a format /dynamic


    # pass  # If it has to be empty for the moment#


#  INSTANCES OF THE CLASS
emp_1 = Employee('Evangelos', 'Germenis',50000)

emp_2 = Employee('Test', 'User', 60000)


# print(emp_1)
# print(emp_2)

#  Variables of an instance / Manual assignments

# emp_1.first = 'Evan'
# emp_1.last = 'Germ'
# emp_1.email = 'evangeloit@gmail.com'
# emp_1.pay = 50000
#
# emp_2.first = 'Test'
# emp_2.last = 'User'
# emp_2.email = 'Test.User@gmail.com'
# emp_2.pay = 60000

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())
print(emp_2.fullname())

# Instance and call method / You don't need to pass self ass an argument

print (emp_1.fullname())

#Call method on the class / You need to pass in the instance as an argument
print (Employee.fullname(emp_1))
