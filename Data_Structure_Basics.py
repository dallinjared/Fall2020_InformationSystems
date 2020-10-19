# Names: Dallin Jared, Huy Doan, True Fullmer, Royce Cotcher
# Description: We are the owners of a very successful hamburger restaurant. Our faithful customers
# line up every day and eat dozens of burgers. We are writing a program to track exactly
# how many hamburgers each customer eats. To do this we will program the followng: Create a variable for a Queue with items of type string.
# This variable will represent your line of customers waiting outside. Create a variable for a Dictionary with keys of type string and values
# of type int. This variable will hold information about each customer. Put 100 customers into the queue. You can use the random class to
# generate random people for your line. Add a random number of burgers to the total for each customer.
# Make sure there is a key in the dictionary for each customer before you try incrementing their
# total! Print out each customer and their total burgers eaten.

# importing the modules that we need
import random
import collections

# Make our functions
# This particular function is used to create a random-ish list of clients


def randomName():
    asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander",
                   "Dusty Bottoms", "Harry Flugleman", "Carmen", "Visible Arrowsman", "Invisible Swordsman", "Singing Bush", "El loco", "El Vato", "El guay"]
    iRandomNum = random.randint(0, 8)
    return asCustomers[iRandomNum]
# This function will randomly assign a number of burgers to each costumer.... cause that's how capitalism works


def randomBurgers():
    return random.randint(1, 1)


# Create our data structures
queue = []
dCustomer = {}

# Here we are calling the randomName function to be able to create our queue out of a list of random-ish names
for iCount in range(0, 100):
    queue.append(randomName())

# Here we are assigning burgers to each customer
while len(queue) > 0:
    for name in queue:
        if name not in dCustomer:
            dCustomer[name] = randomBurgers()
        else:
            dCustomer[name] += randomBurgers()

        queue.pop(0)

# Here we are sorting the dictionary into desending order
listSortedCustomers = sorted(
    dCustomer.items(), key=lambda x: x[1], reverse=True)

# print out the list of clients
for key, value in listSortedCustomers:
    print(key + ": " + str(value))
