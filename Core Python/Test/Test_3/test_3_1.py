# WAP to print first n prime numbers.


num = int(input("Enter a number :"))

for i in range(1,num+1):
    if(i%2!=0):
        print(i)