# This is the very first task to be done
# Day 1 - Working with Variables in Python to Manage Data
# Concepts Practiced
# Printing to the Console in Python
# String Manipulation and Code Intelligence
# Debugging
# The Python Input Function
# Python Variables
# Variable Naming

# Band Name Generator

welcomeNote = "Welcome to the \"Band Name Generator\"\nA \
platform created to help you generate band names.\n\
To generate the Band Name, please answer these brief questions:\n"
name = input("Welcome, Please Enter name: \n")

print(f"Hello {name}, {welcomeNote}")

city = input("What city did you grow up in?\n")
petName = input("What's the name of your first pet?\n")

bandName = petName+city

print(f"The name of your band should be \n{bandName}")
