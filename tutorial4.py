# # Question 1 -
# i = 0
# while i<=10:
#     print(i, end=" ")
#     i = i + 1

# # Question 2 -
# i = 2
# while i <= 20:
#     print(i, end=" ")
#     i = i + 2

# # Question 3 -
# i = 2
# while i <= 30:
#     print("*", end=" ")
#     i = i + 1

# # Question 4 -
# n = int(input("Enter the value of n: "))
# while n >= 0:
#     print(n, end=" ")
#     n = n - 1

# # Question 5 - Write a program to read the numbers until -1 is read. Also, count the negatives, positives,
# # and zeros entered by the user.
# num = eval(input("Enter your value('-1' to stop): "))
# while True:
#     if num == -1:
#         break
#     elif num > 0:
#         print("It is a positive number.")
#     elif num < 0:
#         print("It is a negative number.")
#     elif num == 0:
#         print("It is a Zero")
#     num = eval(input("Enter your value('-1' to stop): "))

# # Question 6- Write a program to read the numbers until -1 is encountered. Find the average of positive numbers
# # and negative numbers entered by the user. (DIY)
# num = eval(input("Enter your value('-1' to stop): "))
# numbers = []
# while True:
#     if num == -1:
#         break
#     numbers.append(num)
#     num = eval(input("Enter your value('-1' to stop): "))
#
# # print(numbers)
# avg = sum(numbers) / len(numbers)
# print("Average of all input numbers: ", avg)

# # Question 7- Write a program to find whether the given number is an Armstrong number
# def is_armstrong_number(num):
#     num_str = str(num)
#     num_length = len(num_str)
#     total_sum = 0
#     for n in num_str:
#         total_sum += int(n) ** num_length
#     return total_sum == number
#
#
# number = int(input("Enter you number: "))
#
# if is_armstrong_number(number):
#     print(f"{number} is an Armstrong number")
# else:
#     print(f"{number} is not an Armstrong number")

# # Question 8
# num1 = eval(input("Enter your first number"))
# num2 = eval(input("Enter your second number"))
# num = num1 + num2
# total_sum = num
# num3 = 0
# while True:
#     num3 = eval(input("Enter another value"))
#     total_sum += num3
#     print(total_sum)
#     prompt = input("Don you want to add more? ").lower()
#     if prompt == "no":
#         break
# print(f"Your total sum is {total_sum}")

# # Question 9
# def gcd(a, b):
#     if b == 0:
#         return a
#     else:
#         return gcd(b, a % b)

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# print("The GCD of", num1, "and", num2, "is", gcd(num1, num2))



# # Question 10
# i = 0
# while i < 10:
#     i = i + 1
#     if(i == 5):
#         print("\n Continue")
#         continue
#     if(i == 7):
#         print("\n Breaking")
#         break
#     print(i, end=" ")
# print("\n Done")

# # Question 11
# # Initialize counters
# upper_count = 0
# lower_count = 0
# num_count = 0

# # Loop until user enters "*"
# while True:
#     # Read input from user
#     char = input("Enter a character: ")

#     # Check if user entered "*"
#     if char == "*":
#         break

#     # Increment appropriate counter based on input type
#     if char.isupper():
#         upper_count += 1
#     elif char.islower():
#         lower_count += 1
#     elif char.isdigit():
#         num_count += 1

# # Print counts
# print("Uppercase count:", upper_count)
# print("Lowercase count:", lower_count)
# print("Number count:", num_count)


# # Question 12
# numbers = [11, 22, 33, 44, 55]
# index = 1
# while(index<len(numbers)):
#     print(numbers[index])
#     index+=1
#     break

# # Question 13
# numbers = [11, 22, 33, 44, 55, 66]
# index = 2
# while(index<len(numbers)):
#     print(numbers[index], end=" ")
#     index += 1
#     continue

# # Question 14
# list3 = list(range(90, 110))
# i = 0
# while(i<len(list3)):
#     print(list3[i], end=" ")
#     i += 1

# # Question 15
# i = 1
# while i < 5:
#     print(i)
#     i += 1
#     if i == 3:
#         break
# else:
#     print("This won't be printed")