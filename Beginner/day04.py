import random


# result = random.randint(1, 5000)
# if result % 2 == 0:
#     print("Tails")
# else:
#     print("Heads")

# ____________________________________________________________


# Banker Roulette

# names = input("Please enter your names separated bu a ',' and a space:\n")
# name_list = names.split(", ")

# index = random.randint(0, len(name_list - 1))
# print(f"{name_list[index]} is going to pay for today's meal")

# ____________________________________________________________


# Treasure Map

r1 = ["🔲", "🔲", "🔲"]
r2 = ["🔲", "🔲", "🔲"]
r3 = ["🔲", "🔲", "🔲"]

map = [r1, r2, r3]
print(f"{r1}\n{r2}\n{r3}\n")

position = input("Where do you want to put the treasure?\n")
column = int(position[0]) - 1
row = int(position[1]) - 1

# map[column] = "X"
# map[row] = "X"

map[row][column] = "X"

print(f"{r1}\n{r2}\n{r3}\n")
