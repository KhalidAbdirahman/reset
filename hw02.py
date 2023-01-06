import math

#TODO: Fill out the Purpose, Parameter(s), and Return Value
# for each of the two functions below in comments, and then write
# additional functions for parts B and C, and fill out the same information
# for those functions as well.

# Example functions for background reading

# def nickels_to_cents(nickels):
#     '''
#     Purpose:
#         Converts from a given number of nickels to
#         the number of cents they represent
#     Parameter(s):
#         nickels: The number of nickels we have
#     Return Value:
#         The amount in cents we have
#     '''
#     total = nickels * 5
#     return total

# def degrees_to_radians(deg):
#     '''
#     Purpose:
#         Converts from degrees to radians
#     Parameter(s):
#         deg: The number of degrees in a given angle
#     Return Value:
#         The given angle's measure in radians
#     '''
#     radians = deg * math.pi / 180
#     return radians




# Part A: Two functions that you should add documentation to
def celsius_to_fahrenheit(celsius):
    '''
    Purpose:
        Coverts from celsius to fahrenheit
    Parameter(s):
        celcius: The temperature of a place in celsius
    Return Value:
        The temperature of a place in fahrenheit
    '''
    fahr = (celsius * 9 / 5) + 32
    return fahr

def print_25_stars():
    '''
    Purpose:
    Parameter(s):
    Return Value:
    '''
    print('*****')
    print('*****')
    print('*****')
    print('*****')
    print('*****')
    

# Part B: Write out a few simple conversions

def circumference_circle(radius):
    '''
    Purpose:
        Finds the circumference of a circle
    Parameter:
        radius: The value of a circle's radius
    Return Value:
        circumference of a circle
    '''
    circumference_circle = 2 * math.pi * radius
    return circumference_circle

def gallons_to_liters(gallons):
    '''
    Purpose:
        To convert gallons to liters
    Parameter:
        gallons: total gallons of water
    Return Value:
        total liters of water
    '''
    liters = gallons * 3.7854
    return liters

    
def days_to_minutes(days):
    '''
    Purpose:
        To convert days to minutes
    Parameter:
        days: total days
    Return Value:
        total minutes
    '''
    minutes = days * 1440
    return minutes



# Part C: Calculate cost of an ice skating field trip

def trip_cost(students, teachers, own_skates):
    '''
    Purpose:
        To estimate the cost of the trip
    Parameter:
        students: the number of students going on the trip 
        teachers: the number of teachers going on the trip
        own_skates: the number of students coming with their own skateboards
    Return Value:
        Bus cost, Lunch cost and Rental cost  
    '''
    bus_cost = (math.ceil((students + teachers) / 50) * 200)
    skate_rental = ((students * 4) - (own_skates * 4))
    students_lunch = (students * 5)
    teachers_lunch = (teachers * 7)
    lunch = students_lunch + teachers_lunch
    trip_cost = bus_cost + skate_rental + students_lunch + teachers_lunch
    print ('Bus cost: ', bus_cost)
    print ('Lunch cost: ', lunch )
    print ('Rental cost: ',skate_rental)
    return trip_cost
    



    
