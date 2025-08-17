# WAP to check if a given number is Armstrong number or not, 
# for each task create separate function.

def arm_strong (num):

    temp = num
    sum = 0

    while(num>0):

        digit = num%10
        sum +=digit**3
        num //=10

    if(temp == sum):
        print("It is armstrong.")
    else:
        print("It is not armstrong.")

num = int(input("Enter a number :"))

arm_strong(num)