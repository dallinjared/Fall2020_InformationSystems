# Pet Boarding OOP Assignment (Huy Doan, True Fullmer, Dallin Jared, Royce Cotcher)
# This program is written to help our Pet Boarding Company collect information
# on our customers and the pets they bring into our care. We'll collect info about
# them, their pet, and appointment details so we know which pets are in our care,
# who they belong to, how to contact them, and how much we're owed for our services.

from datetime import datetime


class Appointment:
    def __init__(self):
        self.begin_date
        self.end_date
        self.day_rate
        self.total_days
        self.total_cost
        # self.owner = owner

    def set_appointment(self, begin_date, end_date, day_rate):
        self.begin_date = begin_date
        self.end_date = end_date
        self.day_rate = day_rate
        self.calc_days()
        # self.balance

    def calc_days(self):
        self.total_days = (self.end_date - self.begin_date).days
        self.total_cost = total_days * self.day_rate


class Pet:
    def __init__(self, sPetName, sBreed, iAge):
        self.pet_name = sPetName
        self.breed = sBreed
        self.age = iAge
        self.appointment = None

    def get_pet_info(self):
        return (self.pet_name + ' ' + self.breed + ' ' + self.age)

    # Name the company
    company_name = "Critter Watch"
    # create the constructor and inicialize the instance varables


class Customer:
    def __init__(self, sFirstName, sLastName, sAddress1, sAddress2, sCity, sState, sZip):
        self.first_name = sFirstName
        self.last_name = sLastName
        self.address1 = sAddress1
        self.address2 = sAddress2
        self.city = sCity
        self.state = sState
        self.zip = sZip
        self.balance = 0.0
        self.cust_pet = None
        self.cust_id = None

    def gen_id(self):
        return (self.first_name[0:3] + self.last_name[0:3] + self.address1[0:5]).replace(" ", "")

    def return_bill(self):
        return "Customer " + self.cust_id + " with name " + self.first_name + " " + self.last_name
        + " owes " + self.balance + self.cust_pet.pet_name + " 's stay from "

    def make_payment(self, balance):
        self.fBalance = balance - self.fBalance


# From user, get personal information as it pertains to their address and name
sFirstName = 'Dallin'  # input("Enter the customer first name: ")
sLastName = 'Jared'  # input("Enter the customer last name: ")
sAddress1 = '1234 W 4321 N'  # input("Enter the customer address 1: ")
sAddress2 = 'Apt 321'  # input("Enter the customer address 2: ")
sCity = 'Provo'  # input("Enter the customer city: ")
sState = 'Utah'  # input("Enter the customer state: ")
sZip = '84003'  # input("Enter the customer zip: ")

# Call Customer constructor
oCustomer = Customer(sFirstName, sLastName, sAddress1,
                     sAddress2, sCity, sState, sZip)

oCustomer.cust_id = oCustomer.gen_id()
print(oCustomer.cust_id)

# Call pet contructor and assign a pet object to cust_pet
# From User, get animal information
sPetName = 'Cooper'  # input("Enter the customer's pet name: ")
sPetBreed = 'Porcupine'  # input("Enter the customer's pet breed: ")
iAge = '9'  # input("Enter the customer's pet age: ")

oCustomer.cust_pet = Pet(sPetName, sPetBreed, iAge)

print(oCustomer.cust_pet.get_pet_info())

begin_date = datetime.strptime(
    input("Enter Start date in the format m/d/yyyy: "), "%m/%d/%Y")

end_date = datetime.strptime(
    input("Enter End date in the format m/d/yyyy: "), "%m/%d/%Y")

day_rate = 1.2

oCustomer.cust_pet.appointment = Appointment().set_appointment(
    begin_date, end_date, day_rate)
print(oCustomer.cust_pet.appointment.total_days)
