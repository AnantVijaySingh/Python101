f = open('testDataFiles/someFile.txt', 'r')  # Read mode
file_data = f.read()
f.close()
print(file_data)

f1 = open('testDataFiles/anotherFile.txt', 'w')  # Write mode. If the file does not exist, Python will create one.
f1.write('Hello Ice-cream!')
f.close()
f1 = open('testDataFiles/anotherFile.txt', 'r')
file_data = f1.read()
print(file_data)
f2 = open('testDataFiles/anotherFile.txt', 'a')  # Append mode. This will not overwrite the file as in case of Write mode.
f2.write(' and Chocolate Cake :)')
f2.close()
with open('testDataFiles/anotherFile.txt',
          'r') as f2:  # File is kept open within the context and closed at the end, the varilables are not confined to the context
    file_data = f2.read()
print(file_data)

# Conveniently, Python will loop over the lines of a file using the syntax for line in file instead of having to user
# readLine. We can use this to create a list of lines in the file. Because each line still has its newline character
# attached, we remove this using .strip().

camelot_lines = []
with open("testDataFiles/camelot.txt") as f:
    for line in f:
        camelot_lines.append(line.strip())

print(camelot_lines)


# Question: You're going to create a list of the actors who appeared in the television programme Monty Python's
# Flying Circus. Write a function called create_cast_list that takes a filename as input and returns a list of
# actors' names. It will be run on the file flying_circus_cast.txt

def create_cast_list(filename):
    cast_list_flying_circus = []
    # use with to open the file filename
    # use the for loop syntax to process each line
    # and add the actor name to cast_list
    with open(filename, 'r') as fileVariable:
        for lineElement in fileVariable:
            cast_list_flying_circus.append(lineElement.split(',')[0])

    return cast_list_flying_circus


cast_list = create_cast_list('testDataFiles/flying_circus_cast.txt')
for actor in cast_list:
    print(actor)
