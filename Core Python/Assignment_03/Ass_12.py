# WAP to check if given 3 digit number is a palindrome or not.

num = int(input("Enter a number : "))

temp = num
rev = 0

while(num>0):
        digit = num%10
        rev = rev*10+digit
        num=num//10

        
        
        '''d1 = num//100
        d = num//10
        d2 = d%10
        d3 = num%10'''


if(temp == rev):
    print(f"It is palindrome")
else:
    print(f"It is not palindrome.")