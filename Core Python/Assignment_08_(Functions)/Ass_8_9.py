# WAP to check if entered number is a palindrome or not.

def palindrome (num):

    temp = num
    rev = 0

    while(num>0):

        digit = num%10
        rev = rev*10+digit
        num = num//10

    if(temp == rev):
        print("it's palindrome.")
    else:
        print("it's not palindrome.")

num = int(input("Enter a number : "))

palindrome(num)