# WAP to check if given 3 digit number is a palindrome or not.

num = int(input("Enter a three digit number : "))

d1= num%10
d2 = num//10
d= d2%10
d3 = num//100



reverse_num= (d1*100) + (d*10)+d3

print(f"This is the reverse number is : {reverse_num}")
#print(str(num)[:: -1])