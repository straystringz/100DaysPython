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

# r1 = ["🔲", "🔲", "🔲"]
# r2 = ["🔲", "🔲", "🔲"]
# r3 = ["🔲", "🔲", "🔲"]

# map = [r1, r2, r3]
# print(f"{r1}\n{r2}\n{r3}\n")

# position = input("Where do you want to put the treasure?\n")
# column = int(position[0]) - 1
# row = int(position[1]) - 1

# # map[column] = "X"
# # map[row] = "X"

# map[row][column] = "X"

# print(f"{r1}\n{r2}\n{r3}\n")

# ____________________________________________________________


# Rock Paper Scissors

def display_choice(choice):
    if choice == 0:
        print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
        """)
    elif choice == 1:
        print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
        """)
    elif choice == 2:
        print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
        """)


def usr_choice():
    allowed_choices = [0, 1, 2]
    try:
        n = int(input("What do you choose:\n0: Rock\n1: Paper\n2: Scissors\n"))
        if n not in allowed_choices:
            print("Please choose only numbers between 0, 1, and 2")
            usr_choice()
        else:
            print("Your choice")
            display_choice(n)
            # return n
    except ValueError:
        print("Invalid input! Please enter a number (0, 1, or 2).")
        usr_choice()
    return n


def main():
    user_choice = usr_choice()
    computer_choice = random.randint(0, 2)

    print("Computer's choice")
    display_choice(computer_choice)

    if user_choice == computer_choice:
        print("it's a Draw")
        main()
    elif (user_choice == 1 and computer_choice == 0) or \
        (user_choice == 2 and computer_choice == 1) or \
            (user_choice == 0 and computer_choice == 2):
        print("You win")
    else:
        print("You loose")


main()
