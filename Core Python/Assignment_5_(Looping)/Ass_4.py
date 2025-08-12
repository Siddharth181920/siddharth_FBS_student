'''WAP to check if given number is Armstrong number or not.
(Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 +
4*4*4*4)'''

num= int (input("Enter a number : "))

sum = 0

temp = num

while (temp>0):
    dgt = temp%10
    sum += dgt**3
    temp//=10


if num==sum:
    print("It is armstrong number ")
else:
    print("It is not armongstrong number.")

