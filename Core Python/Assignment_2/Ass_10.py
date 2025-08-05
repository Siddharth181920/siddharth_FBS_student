#WAP to reverse three digit number

num = int(input("Enter the three digit number : "))

d1= num//100
d= num//10
d2 = d%10
d3= num%10

rev_num = (100*d3)+(10*d2)+d1

print(f"the reverse three digit num is : {rev_num}") 