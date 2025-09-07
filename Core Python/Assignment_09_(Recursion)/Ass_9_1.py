# WAP to sum of following series using recursion function.
# i. 1! + 2! + 3! + 4! +..... + n!


def SoS(n):
    if(n==0):
        return 0
    else:
        return n+SoS(n-1)
    
n = 5
sum = SoS(n)
print(sum)