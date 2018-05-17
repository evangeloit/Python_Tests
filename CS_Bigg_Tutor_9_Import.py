

# import my_module as mm

# Import everything
# from my_module import *

import sys
# sys.path.append('path') ## include a path for python / you manipulate it a list

import random # Use of the standard library


from my_module import find_index, test


courses = ['History', 'Math', 'Physics', 'CompSci']

random_course = random.choice(courses)
print(random_course)

index = find_index(courses, 'Math')

# print(index)
# print(test)

print(sys.path) # list of the dirs that python looks for modules when i run import


## use of mopdule of std lib

import math

rads = math.radians(90)

print(math.sin(rads))

import datetime
import calendar

today = datetime.date.today()
print(today)

print(calendar.isleap(2020))

# os module /use of the underlying OS

import os

print(os.getcwd())

print(os.__file__) # show you directory of the os module in the standard lib

# antigravity joke
import antigravity