# a = int(input())
# rev_a = 0
# while a > 0:
#     last_digit = a % 10
#     rev_a = rev_a * 10 + last_digit
#     a = a // 10
# print(rev_a)

n = int(input("Enter a number: "))
for i in str(n)[::-1]:
    print(i, end="")
