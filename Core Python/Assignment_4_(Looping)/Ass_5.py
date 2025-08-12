# WAP to Fibonacci series upto n.
'''
num = int (input("Enter a number : "))

a = 0
b = 1
i = 1

while(i<num):

    c = a+b
    print(c)
    a= b
    b= c

    i +=1


'''

num = int(input("Enter a number : "))

a = 0
b = 1
i =1

for i in range(1, num+1):

    c = a+b
    print(c)
    a= b
    b=c

    i+=1