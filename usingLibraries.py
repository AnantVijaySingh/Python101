# from module_name import object_name
# from module_name import first_object, second_object
# import module_name as new_name
# from module_name import object_name as new_name
# from module_name import *
# import module_name

# A package is simply a module that contains sub-modules. A sub-module is specified with the usual dot notation.
# import package_name.submodule_name


# Importing 3P libraries
# Run in terminal: pip install package_name
# requirements.txt : Track and help install required packages. Auto install using pip install -r requirements.txt
# beautifulsoup4==4.5.1
# bs4==0.0.1
# pytz==2016.7
# requests==2.11.1

# Write a function called generate_password that selects three random words from the list of words word_list and
# concatenates them into a single string.

# Use an import statement at the top
from random import randrange

word_file = "testDataFiles/words.txt"
word_list = []

# fill up the word_list
with open(word_file, 'r') as words:
    for line in words:
        # remove white space and make everything lowercase
        word = line.strip().lower()
        # don't include words that are too long or too short
        if 3 < len(word) < 8:
            word_list.append(word)


# Add your function generate_password here
# It should return a string consisting of three random words
# concatenated together without spaces

def generate_password(password=""):
    for i in range(3):
        password += word_list[randrange(0, len(word_list))]
    return password


# test your function
print(generate_password())

# Question
# Create a function that opens the flowers.txt, reads every line in it, and saves it as a dictionary. The main (
# separate) function should take user input (user's first name and last name) and parse the user input to identify
# the first letter of the first name. It should then use it to print the flower name with the same first letter (from
# dictionary created in the first function).

# Write your code here
flower_dictionary = {}

# HINT: create a dictionary from flowers.txt
with open('testDataFiles/flowers.txt', 'r') as flowers:
    for flower in flowers:
        key = flower.split(':')[0].strip().lower()
        value = flower.split(':')[1].strip()
        flower_dictionary[key] = value


# HINT: create a function to ask for user's first and last name
def get_user_name():
    while True:
        try:
            full_user_name = raw_input('Enter Name: ')
            first_name = full_user_name.strip().split(' ')[0]
            break
        except Exception as e:
            print('Please enter acceptable value for name: ', e)
    return first_name


user_name_starting_letter = get_user_name()[0].lower()
while True:
    if flower_dictionary.get(user_name_starting_letter):
        print(flower_dictionary[user_name_starting_letter])
        break
    else:
        print('Could not find results, please try again')
        user_name_starting_letter = str(get_user_name()[0])

# print the desired output
