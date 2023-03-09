# def func():
#     for i in range(4):
#         print("Hello world")
# func()

# def func(i):
#     print("Hello World", i)
# func(5+2*3)

# def calcFunction(x, y):
#     return x - y

# a = 20
# b = 10
# differ = calcFunction
# print(differ(a, b))
y = 52
def my_func():
    global x
    x=10
    print("Value inside function: ",y)
my_func()
print(x)