# WAP to find print the following fibonacci series using functions:
# 1 1 2 3 5 8 n terms


def fibonacci (num):

    a = 1
    b = 0

    for i in range(num+1):

        c = a+b
        print(c, end=" ")

        a = b
        b = c
    
    return c
num = int(input("Enter a number : "))

res = fibonacci(num)



