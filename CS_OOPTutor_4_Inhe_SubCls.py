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


dev1 = Employee('Evangelos', 'Germenis',50000)
dev2 = Employee('Test', 'Employee', 60000)

print(dev1.email)
print(dev2.email)
