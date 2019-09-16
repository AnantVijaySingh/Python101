num = int(float(input('Enter a number: ')))
print('Hello World ' * num)

# We can also interpret user input as a Python expression using the built-in function eval. This function evaluates a
# string as a line of Python.

result = eval(input("Enter an expression: "))
print(result)


# Question: Imagine you're a teacher who needs to send a message to each of your students reminding them of their
# missing assignments and grade in the class. You have each of their names, number of missing assignments,
# and grades on a spreadsheet and just have to insert them into placeholders in this message you came up with:

names = input("Enter Name Separated by Commas: ")
assignments = input("Number of assignments Separated by Commas: ")
grades = input("Number of assignments Separated by Commas: ")  # get and process input for a list of grades

# message string to be used for each student
# HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to submit before you can graduate. You're current grade is {} and can increase to {} if you submit all assignments before the due date.\n\n"

# write a for loop that iterates through each set of names, assignments, and grades to print each student's message
names_list = names.split(',')
assignments_list = assignments.split(',')
grades_list = grades.split(',')


for name, assignment, grade in zip(names_list, assignments_list, grades_list):
    potential_grade = int(assignment)*2 + int(grade)
    print(message.format(name, assignment, grade, potential_grade))
    # print(message.format(name, assignment, potential_grade))
