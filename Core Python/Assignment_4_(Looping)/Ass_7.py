# WAP to print all integers upto to that are not divisible by 2 and 3 .

num = int (input("Enter a number : "))

for i in range(1, num+1):
    if (num/2!=0 and num/3!=0):
        print(i)

        i +=1
