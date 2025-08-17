#WAP to check if given number strong number .

num = int(input("Enter a number :  "))

temp=num
sum_fact = 0

while (temp>0):
    dgt = temp%10

    fact = 1
    i = 1

    while(i <=dgt):
        fact *=i
        i +=1

    sum_fact += fact
    temp //= 10

if (sum_fact==num):
    print("strong Number ")
else:
    print("Not strong Number ")
