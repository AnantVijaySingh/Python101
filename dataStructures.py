# Data structures are containers that organize and group data types together in different ways.
list_of_random_things = [1, 3.4, 'a string', True]  # List can contain any combination of data types
print(list_of_random_things[0])
print(list_of_random_things[-1])  # Access the list from the end

# Slicing
# Slicing can support negative indexes
# Slicing can be user to update a section of a list
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', ' Nov', 'Dec'];
third_quarter = months[6:9]  # Lower bound index is included and upper bound is excluded
print(third_quarter)
first_half = months[:6]  # When starting from the first index, the lower bound can be excluded
print(first_half)
last_half = months[6:]
print(last_half)
print(len(months))  # length of a list
months[0:2] = ['Pre birthday', 'birthday']
print(months[:2])

# Membership operators 'in'  and 'not in'
greeting = 'Hello World'
print('ello' in greeting)
print('May' not in months)

months[4] = 'Friday'  # Update a list
print(months[3:5])

# Mutability is about whether or not we can change an object once it has been created. If an object (like a list or
# string) can be changed (like a list can), then it is called mutable. However, if an object cannot be changed with
# creating a completely new object (like strings), then the object is considered immutable.

# Order is about whether the position of an element in the object can be used to access the element. Both strings and
# lists are ordered.


# Print the last three elements of the list
eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']
print(eclipse_dates[-3:])  # Slicing support negative indexes


# List functions
grades = ['B', 'A', 'D', 'C', 'A', 'B']
print(len(grades))
print(max(grades))
print(min(grades))
print(sorted(grades))
print(sorted(grades, reverse=True))
print('-'.join(grades))  # Joins the elements in a list into a string with the defined separator
grades.append('C')
print(grades)


# Tuples are immutable ordered data structures
dimensions = 50, 40, 30  # Parentheses are options when defining tuples
length, breath, height = dimensions  # Tuple unpacking
print('The dimensions are {} x {} x {}'.format(length, breath, height))

