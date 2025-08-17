#WAP to calculate the sum of follwing series where n is input  by user .


n = int (input("Enter a number :"))

m = n

for i in range(1,m):

    if(i/i!=0):
        print(i+i+i)