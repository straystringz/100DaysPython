# fruits = ["mango", "kiwi", "orange", "strawberry"]

# for fruit in range(1, (len(fruits)+1)):
#     print(fruit)


# import math


# student_heights = input("Input a list of students \
# separated by a space: ").split()
# height_sum = 0
# for height in student_heights:
#     height_sum += int(height)

# avg_height = height_sum/len(student_heights)+1
# print(math.ceil(avg_height))


# student_scores = input("Please enter a list of scores \n").split()
# highest_score = 0

# for score in student_scores:
#     if int(score) > highest_score:
#         highest_score = int(score)
# print(f"The highest score in the class is: {highest_score}")


total_num = 0
for num in range(1, 101):
    total_num += num
print(f"The sum of all nums from 1-100 is {total_num}")
