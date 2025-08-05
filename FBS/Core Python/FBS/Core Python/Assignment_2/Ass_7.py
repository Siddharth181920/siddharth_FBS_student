#find the sum of three digit number

num = int(input("Enter the three digit number : "))

d1=num//100
d=num//10
d2= d%10
d3= num%10

add= d1+d2+d3

print(f"the addition of three num is : {add}")