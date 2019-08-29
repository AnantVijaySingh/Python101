# Assigning values to variables
mv_population, mv_size = 74728, 11.995
mv_density = mv_population / mv_size
print(mv_density)

# Assignment operators
mv_population += 4000 - 600
mv_density = mv_population / mv_size
print(mv_density)

# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6

# decrease the rainfall variable by 10% to account for runoff
rainfall *= 0.9

# add the rainfall variable to the reservoir_volume variable
reservoir_volume += rainfall
# increase reservoir_volume by 5% to account for stormwater that flows
# into the reservoir in the days following the storm
reservoir_volume *= 1.05

# decrease reservoir_volume by 5% to account for evaporation
reservoir_volume *= 0.95

# subtract 2.5e5 cubic metres from reservoir_volume to account for water
# that's piped to arid regions.
reservoir_volume -= 2.5e5

# print the new value of the reservoir_volume variable
print(reservoir_volume)

# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------


# Data types
print(type(4))
print(type(4.0))
print(int(49.7))  # Converts to integer
print(float(2 + 1))  # Converts to float

# Because the float, or approximation, for 0.1 is actually slightly more than 0.1, when we add several of them
# together we can see the difference between the mathematically correct answer and the one that Python creates.

print(.1 + .1 + .1 == .3)  # This is false due to the approximation that Python applies


# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------

# Strings
udacity_length = len('udacity')
print(udacity_length)
print(type('string'))

this_string = 'Simon\'s skateboard is in the garage.'  #using delimiters to support ' / " in strings
print(this_string)

# Strings are arrays and can be accessed with  an argument
first_world = 'Hello World'
print(first_world[0])

# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# Data types and conversion

mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"

#TODO: Print a string with this format: This week's total sales: xxx
# You will probably need to write some lines of code before the print statement.

total_sales = int(mon_sales) + int(tues_sales) + int(wed_sales) + int(thurs_sales) + int(fri_sales)  # converting string to int
print("This week's total sales: " + str(total_sales))

# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# String methods
# Print, int, type are functions
# .isLower , .count are methods. Methods work on objects and thus the first argument is the object itself.
# Methods can contain more arguments such as .count(args).

my_string = 'Learning  Python from Udacity'
print(my_string.islower())
print(my_string.count('a'))
print(my_string.find('P'))

print("Beckham has {} balloons".format(27))

animal = "dog"
action = "bite"
print("Does your {} {}?".format(animal, action))

maria_string = "Maria loves {1} and {0}"
print(maria_string.format("math", "statistics"))

"First, thou shalt count to {0}"  # References first positional argument
"Bring me a {}"                   # Implicitly references the first positional argument
"From {} to {}"                   # Same as "From {0} to {1}"
"My quest is {name}"              # References keyword argument 'name'
"Weight in tons {0.weight}"       # 'weight' attribute of first positional arg
"Units destroyed: {players[0]}"   # First element of keyword argument 'players'.

