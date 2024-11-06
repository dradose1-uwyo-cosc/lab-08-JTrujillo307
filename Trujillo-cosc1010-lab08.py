# Jay Trujillo
# UWYO COSC 1010
# Submission Date
# Lab 08
# Lab Section: 15
# Sources, people worked with, help given to:
# Kaleb Moler
# chat gpt (check work)

# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 
def convert_string(value):
    if value.isdigit() or (value[0] == '-' and value[1:].isdigit()):
        return int(value)
    
    if "." in value and value.count(".") == 1:
        integer_part, decimal_part = value.split(".")
        
        if (integer_part.isdigit() or integer_part == "") and decimal_part.isdigit() and len(decimal_part) == 1:
            return float(value)
            
    return False

user_input = input("Please enter an number (integer or float): ")

result = convert_string(user_input)

if result is False:
    print("The number put in is invalid")
else:
    print(f"The converted value is {result}")



print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list
def slope_intercept(m, b, lower_x, upper_x):
    if type(lower_x) != int or type(upper_x) != int:
        return False
    if lower_x > upper_x:
        return False
    y_values = []
    for x in range(lower_x, upper_x + 1):
        y = m * x + b
        y_values.append(y)
    return y_values

def is_valid_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
        
def get_user_input():
    while True:
        m_input = input("Enter slope: ")
        b_input = input("Enter y intercept: ")
        lower_x_input = input("Enter lower x: ")
        upper_x_input = input("Enter upper x : ")
        
        if m_input.lower() == "exit" or b_input.lower() == "exit" or lower_x_input.lower() == "exit" or upper_x_input.lower() == "exit":
            print("Exiting the program.")
            break
        
        if is_valid_number(m_input) and is_valid_number(b_input) and lower_x_input.isdigit() and upper_x_input.isdigit():
            m = float(m_input)
            b = float(b_input)
            lower_x = int(lower_x_input)
            upper_x = int(upper_x_input)
            
            result = slope_intercept(m, b, lower_x, upper_x)
            
            
            if result is False:
                print("This is invalid")
            else:
                print(f"The y-values for the range from {lower_x} to {upper_x} are: {result}")
        else:
            print("invalid try again")
            
get_user_input()

print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null
