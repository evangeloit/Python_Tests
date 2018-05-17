# Functions

#
# def hello_func():
#
#     print('Hello Function.')
#
# # print(hello_func) # Without the parenthesis in the end the func doesn't execute / returns the location in the mem
#
# hello_func()
#
# # keep your code dry
#
# # Return of a func


# def hello_func(greeting, name='You'): # Default value you
#
#     return '{}, {}'.format(greeting, name)

# hello_func()

# print(hello_func().upper())

# Pass arguments in the func

# print(hello_func('Hi',name='Evan'))

# courses = ['Math', 'Art']
# info = {'name': 'john', 'age': 22}
#
# def student_info(*args, **kwargs): # Allowing to accept an arbitrary number of positionla or key words arguments
#     print(args)
#     print(kwargs)
#
# # student_info('MAth', 'Art', name = 'John', age = '22')
#
# student_info(*courses, **info)

## CODE Example ####

# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year."""

    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]


print(days_in_month(2020, 2))