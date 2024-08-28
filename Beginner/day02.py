# Day 2 - Understanding Data Types and How to Manipulate Strings
# Concepts Practiced
# Python Primitive Data Types
# Type Error, Type Checking and Type Conversion
# Data Types
# Mathematical Operations in Python
# Number Manipulation and F Strings in Python
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
