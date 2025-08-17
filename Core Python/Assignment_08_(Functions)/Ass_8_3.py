# WAP to find sum of follwing series using functions.

# a. 1+ 2 + 3 + 4+..... + n

# c. 1^1 + 2^2 + 3^3+ ...... n^n


'''def series (num):

 sum = 0
 for i in range(num+1):
    print(i,end=' ')
    sum +=i
    
    print(f"Series : {sum}")


num = int(input("Enter a number : "))

series( num )
'''

# b. 1!+ 2! + 3! + 4!+..... + n!

'''
def fact (num):

    fact = 1

    for i in range(1,num+1):

        fact *=i
    return fact 

num = int(input("Enter a number : "))

res=fact(num)

print(f"The factorial is : {res}")
'''


# c. 1^1 + 2^2 + 3^3+ ...... n^n

def sum (num):

    num = int(input("Enter a number : "))

    sum = 1

    for i in range(1,num+1):

        sum **=i
    
    return sum


res = sum()

print("The series sum is : {res}")

