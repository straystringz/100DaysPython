# fruits = ["mango", "kiwi", "orange", "strawberry"]

# for fruit in range(1, (len(fruits)+1)):
#     print(fruit)  # Prints the index + 1


# import math


# student_heights = input("Input a list of students \
# separated by a space: ").split()
# height_sum = 0
# counter = 0
# for height in student_heights:
#     height_sum += int(height)
#     counter += 1

# avg_height = height_sum/counter
# print(math.ceil(avg_height))


# Bubble Sort
# student_scores = input("Please enter a list of scores \n").split()
# student_scores = [int(score) for score in student_scores]
# highest_score = 0

# n = len(student_scores) - 1
# for i in range(n):
#     for j in range(0, n - i):
#         if student_scores[j] > student_scores[j + 1]:
#             student_scores[j], student_scores[j + 1] = student_scores[j + 1], \
#                 student_scores[j]
#             print(student_scores)
#     print(j)

# print(student_scores)


# student_scores = input("Please enter a list of scores \n").split()
# student_scores = [int(score) for score in student_scores]
# highest_score = 0

# for score in student_scores:
#     if score > highest_score:
#         highest_score = score
# print(f"The highest score in the class is: {highest_score}")


# total_num = 0
# for num in range(1, 101):
#     total_num += num
# print(f"The sum of all nums from 1-100 is {total_num}")


# Adding Evens
# addEve = 0
# for num in range(1, 101, 2):
#     addEve += num

# print(addEve)


# FizzBuzz
# for i in range(1, 101):
#     if (i % 3 == 0 and i % 5 == 0):
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

import random


alpha_Up = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alpha_Low = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
syms = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']


def passwd_gen(a, b, c, d):
    passwd = []
    for i in range(a):
        passwd.append(random.choice(alpha_Up))
    for i in range(b):
        passwd.append(random.choice(alpha_Low))
    for i in range(c):
        passwd.append(random.choice(nums))
    for i in range(d):
        passwd.append(random.choice(syms))

    random.shuffle(passwd)
    newPass = "".join(passwd)
    with open("passwd.txt", "a") as file:
        file.write(newPass + "\n")

    return newPass


a = int(input("How many Lower case letters would you like?: "))
b = int(input("How many uppercase letters would you like?: "))
c = int(input("How many numbers would you like: "))
d = int(input("How many symbols would you like?: "))

passwd = passwd_gen(a, b, c, d)
print(f"Here's your:\n{passwd}")
