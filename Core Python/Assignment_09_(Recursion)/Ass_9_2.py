# WAP to check if given number is Armstrong number or not using recursive funciton.


def rev_n(num,rev=0):

    if(num==0):
        return rev 
    else:
        return rev_n(num//10,rev*10+num%10)
    
  
def palindrome(num):

    if(num==rev_n(num)):
        print(f"It's palindrome")
    else:
        print(f"It's not palindrome")

num = int(input("Enter a number : "))

palindrome(num)

