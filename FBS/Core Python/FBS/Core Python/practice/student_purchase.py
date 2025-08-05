'''Accept the price from user. Ask the user if he is a student (user may say yes or no ). 
if he is a student and he has purchased more than 500 than discount is 20% otherwise discount is 10% 
. But if he is not a student then if he has purchased more than 600 
discount is 15% otherwise there is not discount.'''


student = str(input("You are student (Yes/No): "))

if(student=='Yes'):
    price = int(input("Enter the book price :  "))
    if(price>=500):
        dis=price/20
        print(f"student buy book and discount price : {dis}")
    else:
        di_1=price/15
        print(f"Your are not student (15%) : {di_1}")
else:
    print(f"Select the desired output.")






