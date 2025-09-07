# WAP to reverse a given number using recursive function.

def rev_n(num,rev = 0):
    
    if(num==0):
        return rev 
    else:
        return rev_n(num//10,rev*10+num%10)

num = int(input("Enter a number :"))
print(f"Reverse number is :",rev_n(num))


