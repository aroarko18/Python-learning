# # Question 1
# num_list = []
# for i in range(2, 20):
#     if (i % 2 == 0 or i % 4 == 0):
#         num_list.append(i)
# print(num_list)

# # Question 2
# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# squareNum = []

# def isSquare(num):
#     for n in num:
#         value = n * n
#         squareNum.append(value)
# isSquare(num)
# print(squareNum)

# total = 0
# for square in squareNum:
#     total += square
# print(total)
# print(filter(isSquare, num))

# # Question 4
# num_list = []
# m = int(input("Enter the starting of the range"))
# n = int(input("Enter the ending of the range: "))
# o = int(input("Enter the steps in the range: "))
# for i in range(m, n, o):
#     num_list.append(i)
# print("Original List: ", num_list)
# num_list.reverse()
# print("Reversed List: ", num_list)

# # Question 5
# def is_positive(x):
#     return x > 0
# numbers = [10, 20, 30, -4, 50, -50]
# print("The original list is, " , numbers)
# positive_numbers = list(filter(is_positive, numbers))
# print("Positive values list = ", positive_numbers)

# # Question 6
# x = [[2, 5, 4],
#      [1, 3, 2],
#      [7, 6, 2]]
# Y = [[1, 7, 4],
#      [7, 3, 2],
#      [4, 0, 9]]
# result = [[0, 0, 0],
#           [0, 0, 0],
#           [0, 0, 0]]
# # print(len(x[0]))
# for i in range(len(x)):
#     for j in range(len(x[0])):
#         result[i][j] = x[i][j] + Y[i][j]
# for r in result:
#     print(r)
    
# # Question 7
# address = "aroarko.sd@gmail.com"
# user_name, domain_name = address.split('@')
# print("User name:", user_name)
# print("Domain name: ", domain_name)

# # Question 8
# Ques = ["Roll_No", "Name", "Course"]
# Ans = [7, "Aro Arko", "Student"]
# for q, a in zip(Ques, Ans):
#     print("What is your ", q, "?")
#     print("My", q, "is:", a)

# Question 9
def sum_pos(*args):
    total = 0
    for i in args:
        if i>0:
            if i>0:
                total += 1
    return total

print()