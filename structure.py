# n = 5
# for i in range(n):
#     for j in range(i+1, n):
#         print(" ", end="")
#     for k in range(i+1):
#         print("*", end="")
#     print()

# n = 6
# for i in range(n):
#     for j in range(i+1):
#         print(" ", end="")
#     for k in range(i, n-1):
#         print("*", end="")
# #     print()

# n = 5
# for i in range(n):
#     for j in range(i, n-1):
#         print(' ', end="")
#     for k in range(i+1):
#         print('*', end="")
#     for l in range(i):
#         print('*', end="")
#     print()

n = 5
for i in range(n-1):
    for j in range(i):
        print(' ', end='')
    for k in range(n - i):
        print('*', end='')
    for l in range(n-1-i):
        print('*', end='')
    print()

for i in range(n):
    for j in range(i, n-1):
        print(' ', end='')
    for k in range(i):
        print('*', end='')
    for l in range(i+1):
        print('*', end='')
    print()
    
        