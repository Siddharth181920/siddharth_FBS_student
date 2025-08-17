#WAP to print Armstrong number whithin a given range.

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















'''
d1 = num//100
d = num//10
d2= d%10
d3 = num%10


print({d1}, {d2}, {d3})
'''