#WAP to find which numbers are divisible by 7 and multiply by 5 in a given range.

num = int(input("Enter a number to check :"))


for i in range(1,num+1):

    if num % 7==0 and num % 5 ==0:

        print(num)
