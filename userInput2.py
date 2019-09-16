while True:
    try:
        x = int(input('Enter a number: '))
        break
    except ValueError:
        print('Not a valid number')
    except KeyboardInterrupt, ZeroDivisionError:
        print('No input taken')
        break
    finally:
        print('End of input process')
print('Number is ', x)

# ----------------- ----------------- -----------------

def party_planner(cookies, people):
    leftovers = None
    num_each = None
    # TODO: Add a try-except block here to
    #       make sure no ZeroDivisionError occurs.
    try:
        num_each = cookies // people
        leftovers = cookies % people
    except ZeroDivisionError:
        print("Oops, you entered 0 people will be attending.")
        print("Please enter a good number of people for a party.")

    return (num_each, leftovers)


# The main code block is below; do not edit this
lets_party = 'y'
while lets_party == 'y':

    cookies = int(input("How many cookies are you baking? "))
    people = int(input("How many people are attending? "))

    cookies_each, leftovers = party_planner(cookies, people)

    if cookies_each:  # if cookies_each is not None
        message = "\nLet's party! We'll have {} people attending, they'll each get to eat {} cookies, and we'll have {} left over."
        print(message.format(people, cookies_each, leftovers))

    lets_party = str(input("\nWould you like to party more? (y or n) "))


# Accessing error messages
try:
    print('try')  # some code
except ValueError as e:
   # some code
   print("ZeroDivisionError occurred: {}".format(e))


# Exception is just the base class for all built-in exceptions.
try:
    print('try')  # some code
except Exception as e:
   # some code
   print("ZeroDivisionError occurred: {}".format(e))