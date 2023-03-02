# # Question 1
# def swap(a, b):
#     a, b = b, a
#     print("After swap: ")
#     print("First number = ", a)
#     print("Second number = ", b)
    
# # Question 2
# def GCD(x, y):
#     rem = x % y
#     if(rem == 0):
#         return y
#     else: return GCD(y, rem)
# n = int(input("Enter the first number"))
# m = int(input("Enter the second number"))
# print("The GCD of numbers is", GCD(n, m))

# Question 3
def fibonacci(n):
    if (n < 2):
        return 1
    return (fibonacci(n-1) + fibonacci(n-2))
n = int(input())
for i in range(n):
    print(f"Fibonacci {i} = {fibonacci(i)}")