#WAP to swap two numbers using third variable.

num1 = int(input("Enter a num1 : "))
num2 = int(input("Enter a num2 : "))

temp =num1
num1 = num2
num2= temp

print(f"The value of num1 is : {num1}")
print(f"The value of num2 is : {num2}")