# # Question 1: Write a program using for loop to calculate the average of first n natural numbers. 
# num = int(input("Enter the number to which you want to get average value: "))
# sum = 0
# for n in range(1, num + 1):
#     sum += n
# avg = sum / num
# print(f"The average of the first {num} natural number is {avg}")

# # Question 2: Write a program to classify a given number as prime or composite
# num = int(input("Enter a number: "))

# is_prime = True

# if num > 1:
#     for i in range(2, num):
#         if num % 2 == 0:
#             is_prime = False
#             break
#         else:
#             is_prime = True
# if is_prime:
#     print(f"{num} is a composite number.")
# else:
#     print(f"{num} is a prime number.")

# # Question 3: Write a program to calculate the sum of the series 1+1/2+….1/n. 
# num = int(input("Enter the number to which you want to get output: "))
# sum = 0
# for n in range(1, num + 1):
#     sum += 1/n
# print(f"The sum of the series 1 + 1/2 + ... + 1/{n} is {sum:.2f}.")

# # Question 4: Write a program to calculate sum of cubes of numbers from 1 to n. (DIY)
# num = int(input("Enter your number: "))
# sum = 0
# for n in range(1, num+1):
#     sum += n**3
# print(f"Sum of cubes of numbers from 1 to {num} is: {sum}")

# # Question 5: Write a program to calculate the sum of squares of even nos. less than the input number
# num = int(input("Enter a number: "))
# sum = 0
# for n in range(2, num, 2):
#     if num % 2 == 0:
#         sum += n**2
# print(sum)

# # Question 6: Write a program using for loop to find the factorial of a number.
# num = int(input("Enter a number: "))
# def factorial(num):
#     factorial_value = 1
#     for n in range(1, num+1):
#         factorial_value *= n
#     return factorial_value
# print(f"Factorial value of {num} is: {factorial(num)}")

# # Question 7: Write a program to calculate pow(x,n) 
# x = float(input("Enter a value for x: "))
# n = int(input("Enter a value for n: "))

# result = 1

# for i in range(abs(n)):
#     result *= x

# if n < 0:
#     result = 1/result
# print(f"{x} to the power of {n} is {result}.")

# # Question 8: Write a program to print the following pattern.
# # *
# # **
# # ***
# # ****
# # *****

# num = 5
# for i in range(1, num + 1):
#     for j in range(i):
#         print("*", end="")
#     print()

# # Question 9: Write a program to print the following pattern. 
# # 1
# # 1	    2
# # 1     2       3
# # 1     2       3      4
# # 1	    2       3      4      5     

# n = 5
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j, end="\t")
#     print()

# # Question - 10: What will be the output of the following Python code? (DIY)
# x = 'abcd'
# for i in x:
#     print(i.upper())

# # Question 11: What will be the output of the following Python code?
# for i in [1, 2, 3, 4][::-1]:
#     print(i)

# # Question 12: What will be the output of the following Python code?
# x = 'abcd'
# for i in range(len(x)):
#     print(i)

# # Question 13: What will be the output of the following Python code?
# x = ['ab', 'cd']
# for i in x:
#     i.upper()
# print(x)

# # Question 14: What will be the output of the following Python code?
# i=0
# while i<10;
# print(i)
# i+=1

# # Question 15: What will be the output of the following Python code?
# num = 3
# 	if num > 0:
# 		print(“POSITIVE.”)
# print (“This is always printed.”)
