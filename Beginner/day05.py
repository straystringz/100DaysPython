# fruits = ["mango", "kiwi", "orange", "strawberry"]

# for fruit in range(1, (len(fruits)+1)):
#     print(fruit)


import math


student_heights = input("Input a list of students \
separated by a space: ").split()
height_sum = 0
for height in student_heights:
    height_sum += int(height)

avg_height = height_sum/len(student_heights)+1
print(math.ceil(avg_height))