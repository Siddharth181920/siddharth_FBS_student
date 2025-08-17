# WAP to print all numbers in a range divisible by a given number .


num = int(input("Enter a number :"))

i=1

for i in range(1, num+1):

    if(i%num==0):
        print(i)


