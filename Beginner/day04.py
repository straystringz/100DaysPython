import random


# result = random.randint(1, 5000)
# if result % 2 == 0:
#     print("Tails")
# else:
#     print("Heads")

# ____________________________________________________________


# Banker Roulette

names = input("Please enter your names separated bu a ',' and a space:\n")
name_list = names.split(", ")

index = random.randint(0, len(name_list - 1))
print(f"{name_list[index]} is going to pay for today's meal")
