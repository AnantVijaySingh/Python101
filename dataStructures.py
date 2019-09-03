# coding=utf-8
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
dimensions = 50, 40, 30  # Parentheses () are options when defining tuples
length, breath, height = dimensions  # Tuple unpacking
print('The dimensions are {} x {} x {}'.format(length, breath, height))

# A set is a data type for mutable unordered collections of unique elements. One application of a set is to quickly
# remove duplicates from a list.


# Set supports membership operators 'in' and 'not in'. You can add elements to sets using the add method, and remove
# elements using the pop method, similar to lists. Although, when you pop an element from a set, a random element is
# removed. Other operations you can perform with sets include those of mathematical sets. Methods like union,
# intersection, and difference are easy to perform with sets, and are much faster than such operators with other
# containers.

numbers = [1, 2, 6, 3, 1, 1, 6]
unique_numbers = set(numbers)
print(unique_numbers)
unique_numbers.add(4)
unique_numbers.add(3)
print(unique_numbers)
unique_numbers_2 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}  # set literal; could have used set([0,1,2,3...])
print(unique_numbers_2)
print(unique_numbers.union(unique_numbers_2))
print(unique_numbers.intersection(unique_numbers_2))
print(unique_numbers_2.difference(unique_numbers))


# A dictionary is a mutable data type that stores mappings of unique keys to values. Dictionaries can have keys of
# any immutable type, like integers or tuples, not just strings. It's not even necessary for every key to have the
# same type!

elements = {"hydrogen": 1, "helium": 2, "carbon": 6}
print('The atomic number of Helium is {}'.format(elements['helium']))  # print the value mapped to "helium"
elements["lithium"] = 3  # insert "lithium" with a value of 3 into the dictionary
print('carbon' in elements)
print(elements.get('carbon'))
print(elements.get('argon'))  # get function returns none or default value instead of error when the key is not present
print(elements.get('argon', 'element not found'))

# Identity operators:
# 'is' : evaluates if both sides have the same identity
# 'not is' : evaluates if both sides have different identities

n = elements.get("dilithium")
print(n is None)
print(n is not None)


# Compounded Data Structures
elements = {"hydrogen": {"number": 1,
                         "weight": 1.00794,
                         "symbol": "H"},
              "helium": {"number": 2,
                         "weight": 4.002602,
                         "symbol": "He"}}
print(elements['helium']['weight'])

# Adding a new entry to the compounded dictionary
oxygen = {"number":8,"weight":15.999,"symbol":"O"}
elements['oxygen'] = oxygen
print('elements = ', elements)


# Question: Add an 'is_noble_gas' entry to the hydrogen and helium dictionaries
# hint: helium is a noble gas, hydrogen isn't
elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}
elements['hydrogen']['is_noble_gas'] = False
elements['helium']['is_noble_gas'] = True
print(elements)

# Practice questions
verse = "if you can keep your head when all about you are losing theirs and blaming it on you   if you can trust yourself when all men doubt you     but make allowance for their doubting too   if you can wait and not be tired by waiting      or being lied about  don’t deal in lies   or being hated  don’t give way to hating      and yet don’t look too good  nor talk too wise"
print(verse, '\n')

# split verse into list of words
verse_list = verse.split()
print(verse_list, '\n')

# convert list to a data structure that stores unique elements
verse_set = set(verse_list)
print(verse_set, '\n')

# print the number of unique words
num_unique = len(verse_set)
print(num_unique, '\n')

verse_dict =  {'if': 3, 'you': 6, 'can': 3, 'keep': 1, 'your': 1, 'head': 1, 'when': 2, 'all': 2, 'about': 2, 'are': 1, 'losing': 1, 'theirs': 1, 'and': 3, 'blaming': 1, 'it': 1, 'on': 1, 'trust': 1, 'yourself': 1, 'men': 1, 'doubt': 1, 'but': 1, 'make': 1, 'allowance': 1, 'for': 1, 'their': 1, 'doubting': 1, 'too': 3, 'wait': 1, 'not': 1, 'be': 1, 'tired': 1, 'by': 1, 'waiting': 1, 'or': 2, 'being': 2, 'lied': 1, 'don\'t': 3, 'deal': 1, 'in': 1, 'lies': 1, 'hated': 1, 'give': 1, 'way': 1, 'to': 1, 'hating': 1, 'yet': 1, 'look': 1, 'good': 1, 'nor': 1, 'talk': 1, 'wise': 1}

print(verse_dict, '\n')

# find number of unique keys in the dictionary
num_keys = len(set(verse_dict.keys()))
print(num_keys)

# find whether 'breathe' is a key in the dictionary
contains_breathe = verse_dict.get('breathe')
print(contains_breathe)

# create and sort a list of the dictionary's keys
dict_keys = verse_dict.keys()
sorted_keys = sorted(dict_keys)
print(sorted_keys)

# get the first element in the sorted list of keys
print(sorted_keys[0])

# find the element with the highest value in the list of keys
print(sorted_keys[-1])
