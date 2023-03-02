# # Question -1: Write a program to determine whether a person is eligible to vote or not. If not eligible,
# # display how many years are left to be eligible.
# current_year = 2023
# birth_year = int(input("Enter your birth year: "))
# age = current_year - birth_year
#
# if age > 18:
#     print("You are eligible to vote.")
# else:
#     years_left = 18 - age
#     print("You are not eligible to vote. You have ", years_left, "years left")

# # Question -2: Write a program to determine whether the character entered is a vowel or not
# vowel_char = ['a', 'e', 'i', 'o', 'u']
# char = input("Enter your character: ").lower()
# if char in vowel_char:
#     print("It's a vowel")
# else:
#     print("It's not a vowel")

# # Question 3 - Write a program that prompts the user to enter a number from 0 to 30 and then print its interval.
# number = int(input("Enter a number between 0 and 30: "))
#
# if 0 <= number <= 10:
#     print("The number is in the [0, 10] interval.")
# elif 10 < number <= 20:
#     print("The number is in the (10, 20] interval.")
# elif 20 < number <= 30:
#     print("The number is in the (20, 30] interval.")
# else:
#     print("The number is outside the [0, 30] interval.")

# # Question 4 - Write a program to test whether a number entered by the user is negative, positive, or equal to zero.
# user_num = float(input("Enter your number: "))
# if user_num > 0:
#     print("Your entered number is positive.")
# elif user_num < 0:
#     print("Your entered number is negative.")
# else:
#     print("Your entered number is equal to zero.")

# Question 5 - Write a program to get input of his/her salary and then print its grade according to the following scale.
# 8000-10000 C grade
# 10000-13000 B grade
# 13001-15000 A grade

# salary_count = int(input("Enter your salary: "))
# if 8000 <= salary_count <= 10000:
#     print("Your salary grade is C")
# elif 10000 < salary_count <= 13000:
#     print("Your salary grade is B")
# elif 13001 <= salary_count <= 15000:
#     print("Your salary grade is A")
# else:
#     print("Out of range!!!")

# # Question 6 - Write a program to take input from the user and then check whether it is a number or character. If
# # it’s a character, determine whether it’s in uppercase or lowercase.
# input_value = input("Enter your value: ")
# if input_value.isdigit():
#     print("It is a number.")
# elif input_value.isalpha():
#     if input_value.isupper():
#         print("It's a uppercase character.")
#     else:
#         print("It's a lowercase character.")

# # Question 7: Write a program to enter the marks of a student in 4 subjects. Then calculate the total and aggregate
# # and display the grade by the student according to the following scale,
# #
# # 	Aggregate is greater than 75%, grade is A
# # 	Aggregate 60>= and <75, then grade is  A-
# # 	Aggregate 50>= and <60, then grade is B+
# # 	Aggregate 40>= and <50, then grade is B-
# # 	Aggregate 30>= and <40, then grade is C+
# # 	Else the grade is fail.
# sub1_mark = float(input("Enter your first subject number: "))
# sub2_mark = float(input("Enter your second subject number: "))
# sub3_mark = float(input("Enter your third subject number: "))
# sub4_mark = float(input("Enter your fourth subject number: "))
#
# total_marks = sub1_mark + sub2_mark + sub3_mark + sub4_mark
# # print(total_marks)
# aggregate = (total_marks / 400) * 100
# # print(aggregate)
#
# if aggregate >= 75:
#     print("Your grade is A")
# elif 60 <= aggregate < 75:
#     print("Your grade is A-")
# elif 50 <= aggregate < 60:
#     print("Your grade is B+")
# elif 40 <= aggregate < 50:
#     print("Your grade is B-")
# elif 30 <= aggregate < 40:
#     print("Your grade is C+")
# else:
#     print("The grade is fail.")
