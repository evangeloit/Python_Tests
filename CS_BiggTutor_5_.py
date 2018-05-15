# Dictionary

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

print(student['name'])
print(student['courses'])


# add a key

student['phone'] = '555-55555'

# update a key

student['name'] = 'Jane'

# Update Multiple Values

student.update({'name': 'Jane', 'age': 26, 'phone': '666-6666'})
print (student)

# Delete a key

# del student['age']

# or POP

age = student.pop('age')

print(age)

# Keys that don't exist error with return of specific message and type

print(student.get('phone', 'Not_Found'))


# len of dict

print(len(student))
#  print keys of Dict

print(student.keys())

# print values of Dict

print(student.values())

# print items ---values and keys

print(student.items())

# Loop keys -values

for key in student.items():
    print(key)