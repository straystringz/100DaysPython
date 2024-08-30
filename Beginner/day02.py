# Day 2 - Understanding Data Types and How to Manipulate Strings
# Concepts Practiced
# Python Primitive Data Types
# Type Error, Type Checking and Type Conversion
# Data Types
# Mathematical Operations in Python
# Number Manipulation and F Strings in Python

# Finger test: Get the sum of each element in 2 digit num entry

# def sepAdd(num):
#     converted_num = str(num)
#     first_digit = converted_num[0]
#     second_digit = converted_num[1]

#     return int(first_digit) + int(second_digit)


# num = input("Enter a 2 digit number: ")
# print(sepAdd(num))


# Your life in weeks

# age = int(input("What's your current age? \n"))
# rem_age = (90-age)
# months = round(rem_age * 12)
# days = round(rem_age * 365)
# weeks = round(rem_age * 52)

# print(f"You have {days} days, {weeks} weeks and {months} months left")


# Tip Calculator
print("Welcome to the tip calculator!")
totalBill = float(input("Please insert the total bill amount\n$ "))
tip = int(input("Percentage tip do you want to give, 10, 12, or 15?\n% "))
splitBetween = int(input("How many people to split the bill?\n"))

payingTip = totalBill*(tip/100)
totalBillWithTip = totalBill + payingTip

totalBillPerPErson = totalBillWithTip / splitBetween
payment = round(totalBillPerPErson, 2)

print(f"Each person should pay: ${payment}")
