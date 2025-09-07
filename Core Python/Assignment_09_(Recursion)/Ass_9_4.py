#WAP to find the sum of n numbers using recursion.


def sum_n(num):
    sum = 0
    for i in range(1,num+1):
        sum +=i
    return sum 
  

num = int(input("Enter a number :"))
res = sum_n(num)
print(res)