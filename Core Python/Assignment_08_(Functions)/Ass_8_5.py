#WAP to sum of all prime numbers between 1 to n .


def prime (num):


    n = 0

    for i in range(1,num+1):

        if(i%2==0):
            print(i)
            n = n+i

    return n

num = int(input("Enter a number :"))

res = prime (num)

print(f"The addition of even number is : {res}")