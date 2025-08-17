#WAP to find sum of digits of a number 


def di_sum(num):

  
    d1 = num%100
    d = num//10
    d2 = d%10
    d3 = num%10

    print(f" The sum of digits is : {d1+d2+d3}")

num = int(input("Enter a number :"))

di_sum(num)