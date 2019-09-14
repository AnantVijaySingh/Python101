points = 174  # use this input to make your submission

# write your if statement here
if 1 <= points <= 50:
    result = "Congratulations! You won a {}!".format('wooden rabbit')
elif 51 <= points <= 150:
    result = "Oh dear, no prize this time."
elif points >= 151 and points <= 180:
    result = "Congratulations! You won a {}!".format('wafer-thin mint')
else:
    result = "Congratulations! You won a {}!".format('penguin')

print(result)

# '''
# You decide you want to play a game where you are hiding
# a number from someone.  Store this number in a variable
# called 'answer'.  Another user provides a number called
# 'guess'.  By comparing guess to answer, you inform the user
# if their guess is too high or too low.

# Fill in the conditionals below to inform the user about how
# their guess compares to the answer.
# '''
answer = 1
guess = 2

if guess < answer:
    result = "Oops!  Your guess was too low."
elif guess > answer:
    result = "Oops!  Your guess was too high."
elif answer == guess:
    result = "Nice!  Your guess matched the answer!"

print(result)

# '''
# Depending on where an individual is from we need to tax them
# appropriately.  The states of CA, MN, and
# NY have taxes of 7.5%, 9.5%, and 8.9% respectively.
# Use this information to take the amount of a purchase and
# the corresponding state to assure that they are taxed by the right
# amount.
# '''
state = 'CA'
purchase_amount = 100

if state == 'CA':
    tax_amount = .075
    total_cost = purchase_amount * (1 + tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state == 'MN':
    tax_amount = .095
    total_cost = purchase_amount * (1 + tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state == 'NY':
    tax_amount = .089
    total_cost = purchase_amount * (1 + tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

print(result)

# Here are most of the built-in objects that are considered False in Python:
# constants defined to be false: None and False
# zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
# empty sequences and collections: '"", (), [], {}, set(), range(0)


points = 174  # use this as input for your submission

# establish the default prize value to None
result = None

# use the points value to assign prizes to the correct prize names
if 1 <= points <= 50:
    result = 'wooden rabbit'
elif 51 <= points <= 150:
    result = None
elif 151 <= points <= 180:
    result = 'wafer-thin mint'
elif 181 <= points <= 200:
    result = 'penguin'

# use the truth value of prize to assign result to the correct prize
if result:
    result = 'Congratulations! You won a {}!'.format(result)
else:
    result = 'Oh dear, no prize this time.'

print(result)


# For Loop
# range(start, stop, step) is a built-in function used to create an iterable sequence of numbers.

cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
for city in cities:
    print(city.title())

capitalized_cities = []
for city in cities:
    capitalized_cities.append(city.title())
    print(capitalized_cities)

for index in range(len(cities)):
    cities[index] = cities[index].title()  # updating the cities list
print(cities)

for i in (range(3)):
    print('Hello World')

# Write a for loop using range() to print out multiples of 5 up to 30 inclusive
for number in range(31):
    if number % 5 == 0:
        print(number)

for i in range(5,35,5):
    print(i)

# Write a for loop that iterates over the names list to create a usernames list.
names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []
for name in names:
    usernames.append(name.lower().replace(' ', '_'))
print(usernames)

usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

for index in range(len(usernames)):
    usernames[index] = usernames[index].lower().replace(' ', '_')
print usernames

# Write a for loop that iterates over a list of strings, tokens, and counts how many of them are XML tags.
tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

for token in tokens:
    if token.find('<') >= 0 and token.find('>') >= 0:
        count += 1
print(count)

count = 0
for token in tokens:
    if '<' in token and '>' in token:
        count += 1
print(count)

# The below solution takes into account the fact that the position of the arrows need to be at the start and end
for token in tokens:
    if token[0] == '<' and token[-1] == '>':
        count += 1


# Write some code, including a for loop, that iterates over a list of strings and creates a single string, html_str,
# which is an HTML list

items = ['first string', 'second string']
html_str = "<ul>\n"

for i in range(len(items)):
    html_str += '<li>{}</li>\n'.format(items[i])
html_str += '</ul>'
print(html_str)
