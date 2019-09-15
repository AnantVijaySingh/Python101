import math


def cylinder_volume(height, radius):
    """
    :param height:
    :param radius:
    :return: volume
    """
    pi = 3.14159
    return height * pi * radius ** 2


def cylinder_volume(height, radius=5):
    """Calculate volume of the cylinder.

       INPUT:
       height: int. The population of that area
       radius: int or float.

       OUTPUT:
       volume of a cylinder
       """
    pi = 3.14159
    return height * pi * radius ** 2


cylinder_volume(10, 7)  # pass in arguments by position
cylinder_volume(height=10, radius=7)  # pass in arguments by name


# Write a function named readable_timedelta. The function should take one argument, an integer days, and return a
# string that says how many weeks and days that is.

# write your function here
def readable_timedelta(days):
    num_days = days % 7
    num_weeks = int((days - num_days) / 7)
    return '{} week(s) and {} day(s).'.format(num_weeks, num_days)


# test your function
print(readable_timedelta(10))

# We can access the value of the global variable word within this function. However, the value of a global
# variable can not be modified inside the function. If you want to modify that variable's value inside this function,
# it should be passed in as an argument.

egg_count = 0


def buy_eggs(count):
    return count + 12


egg_count = buy_eggs(egg_count)  # assigning value to a global variable


def readable_timedelta(days):
    """
    :param days: number of days
    :return: number of weeks and days
    """

    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)


# Lambda Expressions
# You can use lambda expressions to create anonymous functions.

# map() is a higher-order built-in function that takes a function and iterable as inputs, and returns an iterator
# that applies the function to each element of the iterable.

# filter() is a higher-order built-in function that takes a function and iterable as inputs and returns an iterator
# with the elements from the iterable for which the function returns True.

multiply = lambda x, y: x * y
multiply(4, 7)

print(multiply(4, 7))

# -----------------

numbers = [
    [34, 63, 88, 71, 29],
    [90, 78, 51, 27, 45],
    [63, 37, 85, 46, 22],
    [51, 22, 34, 11, 18]
]

averages = list(map(lambda num_list: sum(num_list) / len(num_list), numbers))
print(averages)

cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

short_cities = list(filter(lambda name: len(name) < 10, cities))
print(short_cities)


# Iterators and Generators

# Iterables are objects that can return one of their elements at a time, such as a list. Many of the built-in
# functions we ve used so far, like 'enumerate,' return an iterator.

# An iterator is an object that represents a stream of data. This is different from a list, which is also an
# iterable, but not an iterator because it is not a stream of data.

# Generators are a simple way to create iterators using functions.
# Example of a generator function called my_range
def my_range(x):
    i = 0
    while i < x:
        yield i
        i += 1


for x in my_range(5):
    print(x)

# Question: Write your own generator function that works like the built-in function enumerate.
lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]


def my_enumerate(iterable, start=0):
    # Implement your generator function here
    count = start
    for element in iterable:
        yield count, element
        count += 1


for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))


# Question: Implement a generator function, chunker, that takes in an iterable and yields a chunk of a specified size
# at a time.

def chunker(iterable, size):
    """Yield successive chunks from iterable of length size."""
    # Implement function here
    for i in range(0, len(iterable), size):
        yield iterable[i:i + size]


for chunk in chunker(range(25), 4):
    print(list(chunk))

# can actually create a generator in the same way you'd normally write a list comprehension, except with parentheses
# instead of square brackets. For example:

sq_list = [x ** 2 for x in range(5)]  # this produces a list of squares

sq_iterator = (x ** 2 for x in range(5))  # this produces an iterator of squares

for i in sq_iterator:
    print(i)


# Project Euler problem 10

def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False


def get_primes(number):
    while True:
        if is_prime(number):
            yield number
        number += 1


def solve_number_10():
    # She *is* working on Project Euler #10, I knew it!
    total = 2
    for next_prime in get_primes(3):
        if next_prime < 2000000:
            total += next_prime
        else:
            print(total)
            return

solve_number_10()


#TODO: Read https://jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/