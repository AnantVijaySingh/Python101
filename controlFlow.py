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

for i in range(5, 35, 5):
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

# Iterating Through Dictionaries with

cast = {
    "Jerry Seinfeld": "Jerry Seinfeld",
    "Julia Louis-Dreyfus": "Elaine Benes",
    "Jason Alexander": "George Costanza",
    "Michael Richards": "Cosmo Kramer"
}

print("Iterating through keys:")
for key in cast:
    print(key)

print("\nIterating through keys and values:")
for key, value in cast.items():  # item method returns tuples of key, value pairs
    print("Actor: {}    Role: {}".format(key, value))

# You would like to count the number of fruits in your basket.
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits, but you do not want to count the other items in your basket.

result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# Iterate through the dictionary
# if the key is in the list of fruits, add the value (number of fruits) to result

for fruit, quantity in basket_items.items():
    if fruit in fruits:
        result += quantity

print(result)

# You would like to count the number of fruits in your basket.
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits and not_fruits.

fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# Iterate through the dictionary
# if the key is in the list of fruits, add to fruit_count.
# if the key is not in the list, then add to the not_fruit_count

for fruit, quantity in basket_items.items():
    if fruit in fruits:
        fruit_count += quantity
    else:
        not_fruit_count += quantity

print(fruit_count, not_fruit_count)

# While loop
# sum(list) adds the items in a list

card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
hand = []

# adds the last element of the card_deck list to the hand list
# until the values in hand add up to 17 or more
while sum(hand) < 17:
    hand.append(card_deck.pop())

print(hand)

# number to find the factorial of
number = 6
# start with our product equal to one
product = 1
# track the current number being multiplied
current = 1

# write your while loop here
# multiply the product so far by the current number
# increment current with each iteration until it reaches number

while current <= number:
    product = product * current
    current += 1

# print the factorial of number
print(product)

# use For loop to make the same calculations
# number to find the factorial of
number = 6
# start with our product equal to one
product = 1

# write your for loop here
for i in range(1, number + 1):
    product = product * i
# print the factorial of number
print(product)

# Suppose you want to count from some number start_num by another number count_by until you hit a final number
# end_num. Use break_num as the variable that you'll change each time through the loop.

start_num = 1  # provide some start number
end_num = 10  # provide some end number that you stop when you hit
count_by = 2  # provide some number to count by
break_num = 0

# write a while loop that uses break_num as the ongoing number to
#   check against end_num

while start_num <= end_num:
    start_num += count_by
break_num = start_num

print(break_num)

# write a condition to check that end_num is larger than start_num before looping
# write a while loop that uses break_num as the ongoing number to
#   check against end_num

if end_num > start_num:
    while start_num <= end_num:
        start_num += count_by
    break_num = start_num
    result = break_num
else:
    result = 'Oops! Looks like your start value is greater than the end value. Please try again.'

print(result)

# Write a while loop that finds the largest square number less than an integerlimit and stores it in a variable
# nearest_square.

limit = 40
num = 0
while (num + 1) ** 2 < limit:
    num += 1
nearest_square = num ** 2

print(nearest_square)

# Your code should add up the odd numbers in the list, but only up to the first 5 odd numbers together. If there are
# more than 5 odd numbers, you should stop at the fifth. If there are fewer than 5 odd numbers, add all of the odd
# numbers.

num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69,
            113, 166]

count_of_odd_nums = 0
sum_of_odd_nums = 0
index = 0

while count_of_odd_nums <= 5 and index < len(num_list):
    if num_list[index] % 2 != 0:
        sum_of_odd_nums += num_list[index]
        count_of_odd_nums += 1
    index += 1

print(sum_of_odd_nums)

# Break and Continue
# Write a loop with a break statement to create a string, news_ticker, that is exactly 140 characters long. You
# should create the news ticker by adding headlines from the headlines list, inserting a space in between each
# headline. If necessary, truncate the last headline in the middle so that news_ticker is exactly 140 characters long.

# HINT: modify the headlines list to verify your loop works with different inputs
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
# write your loop here
for headline in headlines:
    news_ticker += headline + " "
    if len(news_ticker) >= 140:
        news_ticker = news_ticker[:140]
        break

print(news_ticker)

# If the numbers are prime, the code should print "[number] is a prime number." If the number is NOT a prime number,
# it should print "[number] is not a prime number", and a factor of that number, other than 1 and the number itself:
# "[factor] is a factor of [number]".

# Your code should check if each number in the list is a prime number
check_prime = [26, 39, 51, 53, 57, 79, 85]

# iterate through the check_prime list
for num in check_prime:

    # search for factors, iterating through numbers ranging from 2 to the number itself
    for i in range(2, num):
        if (num % i) == 0:
            print("{} is NOT a prime number, because {} is a factor of {}".format(num, i, num))
            break
        # otherwise keep checking until we've searched all possible factors, and then declare it prime
        if i == num - 1:
            print("{} IS a prime number".format(num))

# Zip and Enumerate

# Zip returns an iterator that combines multiple iterables into one sequence of tuples. Each tuple contains the
# elements in that position from all the iterables.
# list(zip(['a', 'b', 'c'], [1, 2, 3])) would output [('a', 1), ('b', 2), ('c', 3)].

letters = ['a', 'b', 'c']
nums = [1, 2, 3]

for letter, num in zip(letters, nums):
    print("{}: {}".format(letter, num))

# In addition to zipping two lists together, you can also unzip a list into tuples using an asterisk.
some_list = [('a', 1), ('b', 2), ('c', 3)]
letters, nums = zip(*some_list)  # creates tuples, not lists

# Enumerate is a built in function that returns an iterator of tuples containing indices and values of a list. You'll
# often use this when you want the index along with each element of an iterable in a loop.

letterss = ['a', 'b', 'c', 'd', 'e']
for i, letter in enumerate(letterss):
    print(i, letter)

# Use zip to write a for loop that creates a string specifying the label and coordinates of each point and appends it
# to the list points. Each string should be formatted as label: x, y, z

x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
# write your for loop here
for x, y, z, label in zip(x_coord, y_coord, z_coord, labels):
    points.append('{}: {}, {}, {}'.format(label, x, y, z))

for point in points:
    print(point)

# Use zip to create a dictionary cast that uses names as keys and heights as values

cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]
cast = {}

for name, height in zip(cast_names, cast_heights):
    cast[name] = height

print(cast)

# Unzip the cast tuple into two names and heights tuples.

cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))
# define names and heights here

names, heights = zip(*cast)

print(names)
print(heights)

# Use zip to transpose data from a 4-by-3 matrix to a 3-by-4 matrix
data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

data_transpose = tuple(zip(*data))
print(data_transpose)

# Use enumerate to modify the cast list so that each element contains the name followed by the character's
# corresponding height. For example, the first element of cast should change from "Barney Stinson" to "Barney Stinson
# 72".

cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]

# write your for loop here
for i, name in enumerate(cast):
    cast[i] = "{} {}".format(name, str(heights[i]))

print(cast)

# List Comprehensions: List comprehensions allow us to create a list using a for loop in one step.

# Conditionals in List Comprehensions: You can also add conditionals to list comprehensions (listcomps). After the
# iterable, you can use the if keyword to check a condition in each iteration. If you would like to add else,
# you have to move the conditionals to the beginning of the listcomp,

capitalized_cities = [city.title() for city in cities]
print(capitalized_cities)

squares = [x ** 2 for x in range(9) if x % 2 == 0]
print(squares)

squares = [x ** 2 if x % 2 == 0 else x + 3 for x in range(9)]
print(squares)

# Use a list comprehension to create a new list first_names containing just the first names in names in lowercase.
names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [name.split(' ')[0].lower() for name in names]
print(first_names)

# Use a list comprehension to create a list multiples_3 containing the first 20 multiples of 3.
multiples_3 = [num * 3 for num in range(1, 21)]
print(multiples_3)

# Use a list comprehension to create a list of names passed that only include those that scored at least 65.
scores = {
    "Rick Sanchez": 70,
    "Morty Smith": 35,
    "Summer Smith": 82,
    "Jerry Smith": 23,
    "Beth Smith": 98
}

passed = [name for name in scores.keys() if scores[name] >= 65]
passed = [name for name, score in scores.items() if score >= 65]  # Alternative solution
print(passed)

# Question 1.
# A. Create a dictionary that includes the count of Oscar nominations for each director in the nominations list.
# B. Provide a dictionary with the count of Oscar wins for each director in the winners list.

nominated = {1931: ['Norman Taurog', 'Wesley Ruggles', 'Clarence Brown', 'Lewis Milestone', 'Josef Von Sternberg'],
             1932: ['Frank Borzage', 'King Vidor', 'Josef Von Sternberg'],
             1933: ['Frank Lloyd', 'Frank Capra', 'George Cukor'],
             1934: ['Frank Capra', 'Victor Schertzinger', 'W. S. Van Dyke'],
             1935: ['John Ford', 'Michael Curtiz', 'Henry Hathaway', 'Frank Lloyd'],
             1936: ['Frank Capra', 'William Wyler', 'Robert Z. Leonard', 'Gregory La Cava', 'W. S. Van Dyke'],
             1937: ['Leo McCarey', 'Sidney Franklin', 'William Dieterle', 'Gregory La Cava', 'William Wellman'],
             1938: ['Frank Capra', 'Michael Curtiz', 'Norman Taurog', 'King Vidor', 'Michael Curtiz'],
             1939: ['Sam Wood', 'Frank Capra', 'John Ford', 'William Wyler', 'Victor Fleming'],
             1940: ['John Ford', 'Sam Wood', 'William Wyler', 'George Cukor', 'Alfred Hitchcock'],
             1941: ['John Ford', 'Orson Welles', 'Alexander Hall', 'William Wyler', 'Howard Hawks'],
             1942: ['Sam Wood', 'Mervyn LeRoy', 'John Farrow', 'Michael Curtiz', 'William Wyler'],
             1943: ['Michael Curtiz', 'Ernst Lubitsch', 'Clarence Brown', 'George Stevens', 'Henry King'],
             1944: ['Leo McCarey', 'Billy Wilder', 'Otto Preminger', 'Alfred Hitchcock', 'Henry King'],
             1945: ['Billy Wilder', 'Leo McCarey', 'Clarence Brown', 'Jean Renoir', 'Alfred Hitchcock'],
             1946: ['David Lean', 'Frank Capra', 'Robert Siodmak', 'Clarence Brown', 'William Wyler'],
             1947: ['Elia Kazan', 'Henry Koster', 'Edward Dmytryk', 'George Cukor', 'David Lean'],
             1948: ['John Huston', 'Laurence Olivier', 'Jean Negulesco', 'Fred Zinnemann', 'Anatole Litvak'],
             1949: ['Joseph L. Mankiewicz', 'Robert Rossen', 'William A. Wellman', 'Carol Reed', 'William Wyler'],
             1950: ['Joseph L. Mankiewicz', 'John Huston', 'George Cukor', 'Billy Wilder', 'Carol Reed'],
             1951: ['George Stevens', 'John Huston', 'Vincente Minnelli', 'William Wyler', 'Elia Kazan'],
             1952: ['John Ford', 'Joseph L. Mankiewicz', 'Cecil B. DeMille', 'Fred Zinnemann', 'John Huston'],
             1953: ['Fred Zinnemann', 'Charles Walters', 'William Wyler', 'George Stevens', 'Billy Wilder'],
             1954: ['Elia Kazan', 'George Seaton', 'William Wellman', 'Alfred Hitchcock', 'Billy Wilder'],
             1955: ['Delbert Mann', 'John Sturges', 'Elia Kazan', 'Joshua Logan', 'David Lean'],
             1956: ['George Stevens', 'Michael Anderson', 'William Wyler', 'Walter Lang', 'King Vidor'],
             1957: ['David Lean', 'Mark Robson', 'Joshua Logan', 'Sidney Lumet', 'Billy Wilder'],
             1958: ['Richard Brooks', 'Stanley Kramer', 'Robert Wise', 'Mark Robson', 'Vincente Minnelli'],
             1959: ['George Stevens', 'Fred Zinnemann', 'Jack Clayton', 'Billy Wilder', 'William Wyler'],
             1960: ['Billy Wilder', 'Jules Dassin', 'Alfred Hitchcock', 'Jack Cardiff', 'Fred Zinnemann'],
             1961: ['J. Lee Thompson', 'Robert Rossen', 'Stanley Kramer', 'Federico Fellini', 'Robert Wise',
                    'Jerome Robbins'],
             1962: ['David Lean', 'Frank Perry', 'Pietro Germi', 'Arthur Penn', 'Robert Mulligan'],
             1963: ['Elia Kazan', 'Otto Preminger', 'Federico Fellini', 'Martin Ritt', 'Tony Richardson'],
             1964: ['George Cukor', 'Peter Glenville', 'Stanley Kubrick', 'Robert Stevenson', 'Michael Cacoyannis'],
             1965: ['William Wyler', 'John Schlesinger', 'David Lean', 'Hiroshi Teshigahara', 'Robert Wise'],
             1966: ['Fred Zinnemann', 'Michelangelo Antonioni', 'Claude Lelouch', 'Richard Brooks', 'Mike Nichols'],
             1967: ['Arthur Penn', 'Stanley Kramer', 'Richard Brooks', 'Norman Jewison', 'Mike Nichols'],
             1968: ['Carol Reed', 'Gillo Pontecorvo', 'Anthony Harvey', 'Franco Zeffirelli', 'Stanley Kubrick'],
             1969: ['John Schlesinger', 'Arthur Penn', 'George Roy Hill', 'Sydney Pollack', 'Costa-Gavras'],
             1970: ['Franklin J. Schaffner', 'Federico Fellini', 'Arthur Hiller', 'Robert Altman', 'Ken Russell'],
             1971: ['Stanley Kubrick', 'Norman Jewison', 'Peter Bogdanovich', 'John Schlesinger', 'William Friedkin'],
             1972: ['Bob Fosse', 'John Boorman', 'Jan Troell', 'Francis Ford Coppola', 'Joseph L. Mankiewicz'],
             1973: ['George Roy Hill', 'George Lucas', 'Ingmar Bergman', 'William Friedkin', 'Bernardo Bertolucci'],
             1974: ['Francis Ford Coppola', 'Roman Polanski', 'Francois Truffaut', 'Bob Fosse', 'John Cassavetes'],
             1975: ['Federico Fellini', 'Stanley Kubrick', 'Sidney Lumet', 'Robert Altman', 'Milos Forman'],
             1976: ['Alan J. Pakula', 'Ingmar Bergman', 'Sidney Lumet', 'Lina Wertmuller', 'John G. Avildsen'],
             1977: ['Steven Spielberg', 'Fred Zinnemann', 'George Lucas', 'Herbert Ross', 'Woody Allen'],
             1978: ['Hal Ashby', 'Warren Beatty', 'Buck Henry', 'Woody Allen', 'Alan Parker', 'Michael Cimino'],
             1979: ['Bob Fosse', 'Francis Coppola', 'Peter Yates', 'Edouard Molinaro', 'Robert Benton'],
             1980: ['David Lynch', 'Martin Scorsese', 'Richard Rush', 'Roman Polanski', 'Robert Redford'],
             1981: ['Louis Malle', 'Hugh Hudson', 'Mark Rydell', 'Steven Spielberg', 'Warren Beatty'],
             1982: ['Wolfgang Petersen', 'Steven Spielberg', 'Sydney Pollack', 'Sidney Lumet', 'Richard Attenborough'],
             1983: ['Peter Yates', 'Ingmar Bergman', 'Mike Nichols', 'Bruce Beresford', 'James L. Brooks'],
             1984: ['Woody Allen', 'Roland Joffe', 'David Lean', 'Robert Benton', 'Milos Forman'],
             1985: ['Hector Babenco', 'John Huston', 'Akira Kurosawa', 'Peter Weir', 'Sydney Pollack'],
             1986: ['David Lynch', 'Woody Allen', 'Roland Joffe', 'James Ivory', 'Oliver Stone'],
             1987: ['Bernardo Bertolucci', 'Adrian Lyne', 'John Boorman', 'Norman Jewison', 'Lasse Hallstrom'],
             1988: ['Barry Levinson', 'Charles Crichton', 'Martin Scorsese', 'Alan Parker', 'Mike Nichols'],
             1989: ['Woody Allen', 'Peter Weir', 'Kenneth Branagh', 'Jim Sheridan', 'Oliver Stone'],
             1990: ['Francis Ford Coppola', 'Martin Scorsese', 'Stephen Frears', 'Barbet Schroeder', 'Kevin Costner'],
             1991: ['John Singleton', 'Barry Levinson', 'Oliver Stone', 'Ridley Scott', 'Jonathan Demme'],
             1992: ['Clint Eastwood', 'Neil Jordan', 'James Ivory', 'Robert Altman', 'Martin Brest'],
             1993: ['Jim Sheridan', 'Jane Campion', 'James Ivory', 'Robert Altman', 'Steven Spielberg'],
             1994: ['Woody Allen', 'Quentin Tarantino', 'Robert Redford', 'Krzysztof Kieslowski', 'Robert Zemeckis'],
             1995: ['Chris Noonan', 'Tim Robbins', 'Mike Figgis', 'Michael Radford', 'Mel Gibson'],
             1996: ['Anthony Minghella', 'Joel Coen', 'Milos Forman', 'Mike Leigh', 'Scott Hicks'],
             1997: ['Peter Cattaneo', 'Gus Van Sant', 'Curtis Hanson', 'Atom Egoyan', 'James Cameron'],
             1998: ['Roberto Benigni', 'John Madden', 'Terrence Malick', 'Peter Weir', 'Steven Spielberg'],
             1999: ['Spike Jonze', 'Lasse Hallstrom', 'Michael Mann', 'M. Night Shyamalan', 'Sam Mendes'],
             2000: ['Stephen Daldry', 'Ang Lee', 'Steven Soderbergh', 'Ridley Scott', 'Steven Soderbergh'],
             2001: ['Ridley Scott', 'Robert Altman', 'Peter Jackson', 'David Lynch', 'Ron Howard'],
             2002: ['Rob Marshall', 'Martin Scorsese', 'Stephen Daldry', 'Pedro Almodovar', 'Roman Polanski'],
             2003: ['Fernando Meirelles', 'Sofia Coppola', 'Peter Weir', 'Clint Eastwood', 'Peter Jackson'],
             2004: ['Martin Scorsese', 'Taylor Hackford', 'Alexander Payne', 'Mike Leigh', 'Clint Eastwood'],
             2005: ['Ang Lee', 'Bennett Miller', 'Paul Haggis', 'George Clooney', 'Steven Spielberg'],
             2006: ['Alejandro Gonzaalez Inarritu', 'Clint Eastwood', 'Stephen Frears', 'Paul Greengrass',
                    'Martin Scorsese'],
             2007: ['Julian Schnabel', 'Jason Reitman', 'Tony Gilroy', 'Paul Thomas Anderson', 'Joel Coen',
                    'Ethan Coen'],
             2008: ['David Fincher', 'Ron Howard', 'Gus Van Sant', 'Stephen Daldry', 'Danny Boyle'],
             2009: ['James Cameron', 'Quentin Tarantino', 'Lee Daniels', 'Jason Reitman', 'Kathryn Bigelow'],
             2010: ['Darren Aronofsky', 'David O. Russell', 'David Fincher', 'Ethan Coen', 'Joel Coen', 'Tom Hooper']}
winners = {1931: ['Norman Taurog'], 1932: ['Frank Borzage'], 1933: ['Frank Lloyd'], 1934: ['Frank Capra'],
           1935: ['John Ford'], 1936: ['Frank Capra'], 1937: ['Leo McCarey'], 1938: ['Frank Capra'],
           1939: ['Victor Fleming'], 1940: ['John Ford'], 1941: ['John Ford'], 1942: ['William Wyler'],
           1943: ['Michael Curtiz'], 1944: ['Leo McCarey'], 1945: ['Billy Wilder'], 1946: ['William Wyler'],
           1947: ['Elia Kazan'], 1948: ['John Huston'], 1949: ['Joseph L. Mankiewicz'], 1950: ['Joseph L. Mankiewicz'],
           1951: ['George Stevens'], 1952: ['John Ford'], 1953: ['Fred Zinnemann'], 1954: ['Elia Kazan'],
           1955: ['Delbert Mann'], 1956: ['George Stevens'], 1957: ['David Lean'], 1958: ['Vincente Minnelli'],
           1959: ['William Wyler'], 1960: ['Billy Wilder'], 1961: ['Jerome Robbins', 'Robert Wise'],
           1962: ['David Lean'], 1963: ['Tony Richardson'], 1964: ['George Cukor'], 1965: ['Robert Wise'],
           1966: ['Fred Zinnemann'], 1967: ['Mike Nichols'], 1968: ['Carol Reed'], 1969: ['John Schlesinger'],
           1970: ['Franklin J. Schaffner'], 1971: ['William Friedkin'], 1972: ['Bob Fosse'], 1973: ['George Roy Hill'],
           1974: ['Francis Ford Coppola'], 1975: ['Milos Forman'], 1976: ['John G. Avildsen'], 1977: ['Woody Allen'],
           1978: ['Michael Cimino'], 1979: ['Robert Benton'], 1980: ['Robert Redford'], 1981: ['Warren Beatty'],
           1982: ['Richard Attenborough'], 1983: ['James L. Brooks'], 1984: ['Milos Forman'], 1985: ['Sydney Pollack'],
           1986: ['Oliver Stone'], 1987: ['Bernardo Bertolucci'], 1988: ['Barry Levinson'], 1989: ['Oliver Stone'],
           1990: ['Kevin Costner'], 1991: ['Jonathan Demme'], 1992: ['Clint Eastwood'], 1993: ['Steven Spielberg'],
           1994: ['Robert Zemeckis'], 1995: ['Mel Gibson'], 1996: ['Anthony Minghella'], 1997: ['James Cameron'],
           1998: ['Steven Spielberg'], 1999: ['Sam Mendes'], 2000: ['Steven Soderbergh'], 2001: ['Ron Howard'],
           2002: ['Roman Polanski'], 2003: ['Peter Jackson'], 2004: ['Clint Eastwood'], 2005: ['Ang Lee'],
           2006: ['Martin Scorsese'], 2007: ['Ethan Coen', 'Joel Coen'], 2008: ['Danny Boyle'],
           2009: ['Kathryn Bigelow'], 2010: ['Tom Hooper']}

# 1A: Create dictionary with the count of Oscar nominations for each director
nom_count_dict = {}
# Add your code here
for year, names_list in nominated.items():
    for name in names_list:
        if name not in nom_count_dict:
            nom_count_dict[name] = 1
        else:
            nom_count_dict[name] += 1

print("nom_count_dict = {}\n".format(nom_count_dict))

# 1B: Create dictionary with the count of Oscar wins for each director
win_count_dict = {}
# Add your code here
for year, names_list in winners.items():
    for name in names_list:
        if name not in win_count_dict:
            win_count_dict[name] = 1
        else:
            win_count_dict[name] += 1

print("win_count_dict = {}".format(win_count_dict))

# For Question 2: Please provide a list with the name(s) of the director(s) with
# the most Oscar wins. The list can hold the names of multiple directors,
# since there can be more than 1 director tied with the most Oscar wins.



# Add your code here
wins = [count for name, count in win_count_dict.items()]
max_wins = max(wins)

most_win_director = [name for name, count in win_count_dict.items() if count == max_wins]

#ALTERNATIVE SECOND PART OF SOLUTION
highest_count = max(win_count_dict.values())

most_win_director = [key for key, value in win_count_dict.items() if value == highest_count]

print("most_win_director = {}".format(most_win_director))




