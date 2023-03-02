a = 0
b = 1
n = int(input())
for i in range(n+1):
    print(a, end=" ")
    result = a + b
    a = b
    b = result