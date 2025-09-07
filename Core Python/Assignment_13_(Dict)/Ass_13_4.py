# Python program to generate a dictionary that contains numbers between(0 to n) in the form (x,x*x)


num = int(input("Enter a number to print in dictinary :"))

series_dict = {}

for i in range(1,num+1):

    series_dict[i]=i*i

print(series_dict)