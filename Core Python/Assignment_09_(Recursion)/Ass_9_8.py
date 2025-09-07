# WAP to check whether the number is prime or not using recursion.


def prime_num(num,i=2):
  
    if(num==i):
        return True
    elif(num%i==0):
        return False
    return prime_num(num,i+1)

num = int(input("Enter a number :"))
if(prime_num(num)):
    print("Yes",num,"Prime Number")
else:
    print("No",num,"Prime number")