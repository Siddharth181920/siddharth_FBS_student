# WAP to find a factorial using recursion.


def fact(n):
    
    for i in range(1,n+1):
        return  n*fact(n-1)
    else:
        return 1
        # if(n==0):
        #     return 1
        # else:
        #     return n*fact(n-1)

n = int(input("Enter a number :"))
s_fact = fact(n)
print(s_fact)