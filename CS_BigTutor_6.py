

language = 'Java'

if language == 'Python':
    print('Lang is Python')
elif language == 'Java':
    print('Lang is Java')
elif language == 'Javascript':
    print('Lang is Javascript')
else:
    print('NO Match')

#Booleans
user= 'Admin'
loggedin = False

if user == 'Admin' or loggedin:
    print('Admin Page')
else:
    print('Bad Creds')

# switch boolean
if not loggedin:
    print('Please login')
else:
    print('Welcome')

#object same id /same object in memory

a = [1, 2, 3]
b = [1, 2, 3]

# Same pos in memmory
# b = a

print(a == b) # True this 2 lists are equal

print(a is b) # False beacuse these are 2 diff objs in memmory

print(id(a))
print(id(b))
print(id(a) == id(b))

# What Py evaluates True or False

# False Values :

# False
# None
# Zero of a numeric type
# An empty sequence, for example [],'', ()
# An empty mapping , For example {}

condition = 'Test'

if condition:
    print('Evaluate to True')
else:
    print('Eval to False')

