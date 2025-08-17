#Write a program to print prime numbers between 1 to 100.

#n = int (input("Enter the number : "))
count = 0
num = 2

while(count <25):

    for i in range(2,num//2+1):
         if(num%i==0):
            break
    
    else:
         print(num)
         count +=1

    num +=1
 