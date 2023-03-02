# # # Slice Operations
#
# # strName = 'Python is_easy!'
# # print(strName)
# # print(strName[0])
# # print(strName[3:9])
# # print(strName[4:])
# # print(strName[-1])
# # print(strName[:5])
# # print(strName * 2)
# # print(strName + "Isn't it?")
#
# # # Lists
# # listLearn = ['a', 'bc', 83, 1.256]
# # print(listLearn)
# # listLearn[1] = 'cd'
# # print(listLearn)
#
# # # Tuples
# # tupLearn = ('a', 'bc', 87, 1.268)
# # print(tupLearn)
# # # tupLearn[1] = 'cd'
# # # print(tupLearn)
#
#
#
# # num = int(input("Enter a number: "))
# # if num == 1:
# #     print((num, "is not a prime number"))
# # elif num > 1:
# #     #check for factors
# #     for i in range(2, num):
# #         if (num % i) == 0:
# #             print(num, "is not a prime number")
# #             print(i, "times", num // i, "is", num)
# #             break
# #         else:
# #             print((num, "is a prime number"))
#
# n = int(input("Enter the number"))
# sum = 0
# for i in range(1,n+1):
#     a = 1.0 / i
# sum = sum + a
# print((sum))
#
# # #named indexes:
# # txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
# # #numbered indexes:
# # txt2 = "My name is {0}, I'm {1}".format("John",36)
# # #empty placeholders:
# # txt3 = "My name is {}, I'm {}".format("John",36)
#
# # print(txt1)
# # print(txt2)
# # print(txt3)
#
#
# # for i in range(0, 6):
# #     if(i <1):
# #         print()
# #     elif(i>0):
# #         print("*" * i)
#
# # for i in range(1,6):
# #     print()
# #     for j in range(1, i+1):
# #         print(j, end=' ')
#
#
# n = int(input("number"))
# avg = 0.0
# s = 0
# for i in range(n+1):
#     s = s + i
# avg = s / i
# print(s)
# print(avg)

# nested loops
# for i in range(5):
#     print()
#     for j in range(i):
#         print("*", end=' ')

# # *****
#   *   *
#   *   *
#   *   *
#   *****

# for letter in "Hello":
#     print(letter, end=" ")
# else:
#     print("Done")

numbers = [1, 2, 4, 3, 6, 5, 7, 10, 9]
# loop through the numbers
for number in numbers:
    # check if the number is even
    if number % 2 == 0:
        pass
    else:
        print('Current number is:', number)
