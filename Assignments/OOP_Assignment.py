# Dallin Jared, Huy Doan, True Fullmer, Royce Cotcher
# Pet Shop Prog OOP Assignment

#import modules
from datetime import datetime

# set up global variables
oTotalCustomers = []

# set up my classes


class Customer:

    # set up any class varibles
    company_name = "Critter Watch"

    def __init__(self, sFirstName, sLastname, sAddress1, sAddress2, sCity, sState, sZip):
        self.first_name = sFirstName
        self.last_name = sLastname
        self.address1 = sAddress1
        self.address2 = sAddress2
        self.city = sCity
        self.state = sState
        self.zip_code = sZip
        self.balance = 0.0
        self.cust_pet = []
        self.cust_id = self.gen_id(sFirstName, sLastname, sAddress1)

    # make the methods
    def gen_id(self, first_name, last_name, address1):
        first_name.replace(" ", "")
        last_name.replace(" ", "")
        address1.replace(" ", "")
        cust_id = first_name[0:3] + last_name[0:3] + address1[0:3]
        return (cust_id)

    def return_bill(self, i, j):
        return (f"Customer {self.cust_id} with the name {self.first_name} {self.last_name} owes {'{:.2f}'.format(self.balance)} for {self.cust_pet[i].pet_name}'s stay from {self.cust_pet[i].appointment[j].begin_date.strftime('%m/%d/%Y')} to {self.cust_pet[i].appointment[j].end_date.strftime('%m/%d/%Y')}  ")

    def make_payment(self, fPayment):
        self.balance = self.balance - fPayment
# Pet Class and Methods


class Pet:
    def __init__(self, pet_name, breed, age, owner):
        self.pet_name = pet_name
        self.breed = breed
        self.age = age
        self.appointment = []
# Appointment Class and Methods


class Appointment:
    def __init__(self, owner):
        self.begin_date = None
        self.end_date = None
        self.day_rate = None
        self.total_days = None
        self.total_cost = None
        self.owner = owner

    # lets make the methods
    def set_appointment(self, begin_date, end_date, day_rate):
        self.begin_date = begin_date
        self.end_date = end_date
        self.day_rate = day_rate
        self.calc_days()
        self.owner.balance = self.total_cost

    def calc_days(self):

        # calculate the total_days
        self.total_days = (self.end_date - self.begin_date).days

        # check if the total_days is <= 0
        if (self.total_days <= 0):
            self.total_days = 1

        # Calculate the total cost
        self.total_cost = (self.total_days * day_rate)


# Get information from the user
iNumOfCust = int(input("\n\nHow many customers will there be today? "))

for i in range(0, iNumOfCust):

    # owner info
    sFirstName = input(
        f"\n\nWhat is the first name of customer number {(i + 1)}? ")
    sLastname = input(
        f"\n\nWhat is the last name of customer number {(i + 1)}? ")
    sAddress1 = input(
        "\n\nWhat is the house number and street name where you live? ")
    sAddress2 = input("\n\nWhat is the appartment number of where you live? ")
    sCity = input("\n\nWhat is the city called in which you live? ")
    sState = input("\n\nWhat state do you live in? ")
    sZip = input("\n\nAdditionally, what is your zip code? ")
    # make cutomer object
    oCustomer = Customer(sFirstName, sLastname, sAddress1,
                         sAddress2, sCity, sState, sZip)

    iNumOfPets = int(
        input(f"\n\nHow many pets does customer number {(i + 1)} have? "))
    for i in range(0, iNumOfPets):
        # pet info
        print("\n\nNow let's get some information about your pet!\n\n")
        pet_name = input("\nWhat is your pet's name? ")
        breed = input("\nWHat is the breed of your pet? ")
        age = input("\nhow old is your pet? ")
        oCustomer.cust_pet.append(Pet(pet_name, breed, age, oCustomer))

    # append that customer object to the more general list of total customers
    oTotalCustomers.append(oCustomer)

    # appointment info
    iNumOfAppoint = int(
        input(f"\n\nHow many appointments does customer number {(i + 1)} have? "))

    j = 0
    for c in range(0, iNumOfAppoint):
        # appointment information
        dBegin_Date = datetime.strptime(
            input("\n\nEnter Start date in the format m/d/yyyy: "), "%m/%d/%Y")
        dEndin_Date = datetime.strptime(
            input("\n\nEnter end date in the format m/d/yyyy: "), "%m/%d/%Y")
        day_rate = float(
            input(f"\n\nWhat is the daily rate for customer number {(i + 1)}? "))
        oTotalCustomers[i].cust_pet[i].appointment.append(
            Appointment(oTotalCustomers[i]))
        oTotalCustomers[i].cust_pet[i].appointment[i].set_appointment(
            dBegin_Date, dEndin_Date, day_rate)

        j = c

    # Print out the recite for customer
    print(oTotalCustomers[i].return_bill(i, j), "\n")

    # check to see if the customer will be paying now
    sPaymentYesOrNo = input(
        f"\n\nDoes customer {(i + 1)} wish to make a payment now? Yes or No: ")

    if (sPaymentYesOrNo.upper() == "YES" or sPaymentYesOrNo.upper() == "Y"):
        fPayment = float(
            input(f"\n\nHow Much will customer {(i + 1)} be paying at this time? "))
    else:
        fPayment = 0

    # call the make_payment method
    oTotalCustomers[i].make_payment(fPayment)

    # call return_bill one more time with most current bill
    print("\n\nThank you for working with us! Your current bill is the following:")
    print(oTotalCustomers[i].return_bill(i, j))
