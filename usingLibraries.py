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
    print('Function Called')
    for i in range(3):
        password += word_list[randrange(0, len(word_list))]
    return password


# test your function
print(generate_password())
