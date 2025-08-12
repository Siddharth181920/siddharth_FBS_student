#WAP to print all even numbers until n.

num = int(input("Enter a number : "))

for num in range(1,num+1):
    
    if(num%2==0):
        print(num)