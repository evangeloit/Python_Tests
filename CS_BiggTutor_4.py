
#  Python examples Tutorial 4

# List , Tuples and sets

courses = ['History', 'Maths', 'Physics', 'CompSci']

courses2 = ['Art', 'Education']


courses.append('Chemistry')

courses.insert(0,'Electron')

########### extend and insert diff in a list

# courses.insert(0,courses2)

courses.extend(courses2)

# Remove - Pop

courses.remove('Maths')

popped = courses.pop()

print popped


#  Sort

nums = [1 , 5, 4, 3 ,2]

# courses.sort(reverse=True)
nums.sort(reverse=True)


#  No Altering the original list sorted Func

sort_cours=sorted(courses)


# Index

print(courses.index('CompSci'))


# True False indexing

print('Mahts' in courses)


print('CompSci' in courses)


# loop for an item

for course in courses:
    print(course)

# Value and Index

for index,course in enumerate(courses, start= 1):
    print(index, course)


# Turn lists in to string and seperate with ',' or ' - ' ..join

course_str = ' - '.join(courses)

print course_str

#  Turn String back in to list

course_list = course_str.split(' - ')

print(course_list)


# Tuples - 'immutable' , 'Mutable

# Mutable

list_1 = ['History', 'Maths', 'Physics', 'CompSci']

list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'

print(list_1)
print(list_2)


# Immutable

tuple_1 = ('History', 'Maths', 'Physics', 'CompSci')

tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# tuple_1[0] = 'Art'  # Tuple does not suppor item assignment

# print(tuple_1)
# print(tuple_2)


#  Sets - ' Values Unordered and have no Duplicates

cs_courses = {'History', 'Maths', 'Physics', 'CompSci', 'Maths'}

print(cs_courses) # Sets delete duplicates

# Check for sharing items between sets --"What courses are these sets have in common'

cs_courses = {'History', 'Maths', 'Physics', 'CompSci'}
art_courses = {'History', 'Maths', 'Art', 'Design'}

# intersection--What they have in common
print(cs_courses.intersection(art_courses))

# diffs

print(cs_courses.difference(art_courses))

#  Union - All courses printed for both sets

print(cs_courses.union(art_courses))


#  Empty List

empty_list = []
empty_list = list()

# Empty tuple

empty_tuple = ()
empty_tuple = tuple()

# Empty Sets

empty_set = {} # This isn't right ! It's a dict.
empty_set = set()



# print(sort_cours)


# print(nums)

# print(courses)
