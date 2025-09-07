# WAP to print fibonacci series using recursion.


def fibonacci(num):

    if(num<=0):
        return "Enter a correct input"
    elif(num==1):
        return 0
    elif(num==2):
        return 1
    else:
        return fibonacci(num-2)+fibonacci(num-1)
    
def fibonacci_series(num):
    if(num<=0):
        print("Enter a correct input")
    else:
        print("Fibonacci Series :")
        for i in range(1,num+1):
            print(fibonacci(i))

num = int(input("Enter a number : "))
fibonacci_series(num)
    