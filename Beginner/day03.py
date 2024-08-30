# # RollerCoaster
# allowed_height = 120
# cannot = "You are not allowed to ride"
# can = "You can ride"
# height = input("Please enter your height in cm: ")

# if int(height) < allowed_height:
#     print(cannot)
# else:
#     print(can)
#     age = int(input("How old are you please? "))

#     if age <= 12:
#         print("You'll have to pay $5 for this ride")
#     elif age <= 18:
#         print("You'll have to pay $7 for this ride")
#     else:
#         print("You'll have to pay $12 for this ride")

# _________________________________________________________________________

# Odd or Even
# num = int(input("Please type the number here: "))
# odd = f"{num} is an odd number"
# even = f"{num} is an even number"

# if num % 2 == 1:
#     print(odd)
# else:
#     print(even)

# _________________________________________________________________________


# BMI calculator, class work

def bmi(weight, height):
    conv_height = float(height)
    conv_weight = float(weight)

    h2 = conv_height**2
    return conv_weight/h2


persons_weight = input("Please input your weight in kg: ")
persons_height = input("Please input your height in meters: ")

print(int(bmi(persons_weight, persons_height)))

# _________________________________________________________________________
