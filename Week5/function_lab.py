# function_lab.py
# This program demonstrates basic functions with parameters and return values.
# Each function is commented to explain what it does.
#Author: Brylan Williamson

# ---------------------------------------------------
# Function 1: add_numbers
# Purpose: Takes two numbers and returns their sum.
# Inputs: num1 (int or float), num2 (int or float)
# Output: Sum of num1 and num2
# ---------------------------------------------------
def add_numbers(num1, num2):
    return num1 + num2


# ---------------------------------------------------
# Function 2: greet
# Purpose: Takes a person's name and returns a greeting message.
# Input: name 
# Output: A greeting message 
# ---------------------------------------------------
def greet(name):
    return "Hello, " + name + "!"


# ---------------------------------------------------
# Function 3: square_number
# Purpose: Takes a number and returns its square.
# Input: value 
# Output: The number squared
# ---------------------------------------------------
def square_number(value):
    return value * value


# ---------------------------------------------------
# Main Program
# This section calls the functions and prints the results.
# ---------------------------------------------------
def main():

    # Call function 1
    total = add_numbers(5, 3)
    print("The sum of 5 and 3 is:", total)

    # Call function 2
    message = greet("Brylan")
    print(message)

    # Call function 3
    squared = square_number(4)
    print("4 squared is:", squared)


# This ensures main() runs when the file is executed
if __name__ == "__main__":
    main()
