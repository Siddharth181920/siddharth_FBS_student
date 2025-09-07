# WAP to find the sum of digits using recursion.


def sum_series(num):
    sum = 0
    for i in range(1,num+1):
        sum +=i
    print(f"Sum of number :",sum)


num = int(input("Enter a number for sum of series :"))
sum_series(num)

