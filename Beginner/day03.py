# # RollerCoaster
# photos = 3
# allowed_height = 120
# le_12 = 5
# le_18 = 7
# ge_18 = 12
# mid_crises = 0
# cannot = "You are not allowed to ride"
# can = "You can ride"
# height = input("Please enter your height in cm: ")

# if int(height) < allowed_height:
#     print(cannot)
# else:
#     print(can)
#     age = int(input("How old are you please? "))
#     pics = input("Do you want a photo? ")

#     if age <= 12:
#         if pics == "yes":
#             print(f"You'll have to pay ${le_12 + photos} for this ride")
#         else:
#             print(f"You'll have to pay ${le_12} for this ride")
#     elif age <= 18:
#         if pics == "yes":
#             print(f"You'll have to pay ${le_18 + photos} for this ride")
#         else:
#             print(f"You'll have to pay ${le_18} for this ride")
#     elif age <= 44:
#         if pics == "yes":
#             print(f"You'll have to pay ${ge_18 + photos} for this ride")
#         else:
#             print(f"You'll have to pay ${ge_18} for this ride")
#     elif age >= 45 and age <= 55:
#         if pics == "yes":
#             print(f"You'll have to pay ${mid_crises + photos} for this ride")
#         else:
#             print(f"You'll have to pay ${mid_crises} for this ride")

# _________________________________________________________________________

# # Odd or Even
# num = int(input("Please type the number here: "))
# odd = f"{num} is an odd number"
# even = f"{num} is an even number"

# if num % 2 == 1:
#     print(odd)
# else:
#     print(even)

# _________________________________________________________________________

# # BMI calculator, class work


# def bmi(weight, height):
#     conv_height = float(height)
#     conv_weight = float(weight)

#     h2 = conv_height**2
#     return conv_weight/h2


# persons_weight = input("Please input your weight in kg: ")
# persons_height = input("Please input your height in meters: ")

# calc_bmi = round(int(bmi(persons_weight, persons_height)))

# under_weight = f"Your bmi is {calc_bmi} you're a little bit underweight"
# normal_weight = f"Your bmi is {calc_bmi} your weight is okay"
# over_weight = f"Your bmi is {calc_bmi} you're a little bit overweight"
# obese = f"Your bmi is {calc_bmi} you need to visit the gym regularly"
# c_obese = f"Your bmi is {calc_bmi} you need a doctor and a dietician"

# if calc_bmi < 18.5:
#     print(under_weight)

# elif calc_bmi > 18.5 and calc_bmi < 25:
#     print(normal_weight)

# elif calc_bmi > 25 and calc_bmi < 30:
#     print(over_weight)

# elif calc_bmi > 30 and calc_bmi < 35:
#     print(obese)

# else:
#     print(c_obese)

# _________________________________________________________________________


# # Leap year

# def check_leap(year):
#     if year % 4 == 0 and year % 100 != 0 and year % 400 == 0:
#         return ("its a leap year")
#     else:
#         return ("It's not a leap year")


# print(check_leap(2023))

# _________________________________________________________________________


# # Pizza Order
# # amount
# small = 15
# medium = 20
# large = 25

# x_cheese = 1

# pep_small = 2
# pep_large = 3

# print("Welcome to Nellyne's Pizza Hut")

# size = input("What size do you want? S, M, or L\n")
# add_pep = input("Would you want some pepperoni? Y or N\n")
# add_cheese = input("Would you want some extra cheese? Y or N\n")

# if size == "S" or size == "s":
#     if add_pep == "Y" or add_pep == "y":
#         if add_cheese == "Y" or add_cheese == "y":
#             print(f"your bill is {small + x_cheese + pep_small}")
#         else:
#             print(f"your bill is {small + pep_small}")
#     else:
#         print(f"your bill is {small}")

# elif size == "M" or size == "m":
#     if add_pep == "Y" or add_pep == "y":
#         if add_cheese == "Y" or add_cheese == "y":
#             print(f"your bill is {medium + x_cheese + pep_large}")
#         else:
#             print(f"your bill is {medium + pep_large}")
#     else:
#         print(f"your bill is {medium}")

# elif size == "L" or size == "l":
#     if add_pep == "Y" or add_pep == "y":
#         if add_cheese == "Y" or add_cheese == "y":
#             print(f"your bill is {large + x_cheese + pep_large}")
#         else:
#             print(f"your bill is {large + pep_large}")
#     else:
#         print(f"your bill is {large}")

# _________________________________________________________________________


# Love Score

print("Welcome to the Love Calculator")

name_one = input("Please enter your love's name: \n")
name_two = input("Please enter your name: \n")

names = name_one.lower() + name_two.lower()

t = names.count("t")
r = names.count("r")
u = names.count("u")
e = names.count("e")

l_ = names.count("l")
o = names.count("o")
v = names.count("v")

name_total_true = t+r+u+e
name_total_love = l_+o+v+e
name_total_true_love = t+r+u+e+l_+o+v+e

love_score = int(str(name_total_true) + str(name_total_love))

print(f"T occurs {t} times\nR occurs {r} times\n\
U occurs {u} times\nE occurs {e} times\nTotal = {name_total_true}\n\n\
L occurs {l_} times\n\
O occurs {o} times\nV occurs {v} times\nE occurs {e} times\n\
Total = {name_total_love}\n")

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score},\
    \nYou go together like coke and mentos.")

elif love_score >= 40 and love_score <= 50:
    print(f"Your Love Score is {love_score},\
    \nYou're alright together.")

else:
    print(f"Your Love Score is {love_score}")
