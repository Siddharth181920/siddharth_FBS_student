#WAP to check if given number is perfect number .


num = int(input("Enter a number :"))
sum = 0
i = 1

while(i < num): 

    if(num%i==0):
        sum +=i
    
    i +=1

if(sum==num):
    print("Perfect Number .")
else:
    print("No perfect number.")
