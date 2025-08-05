#WAP Swap two numbers without using third variable.

num1 = int(input("Enter a num1 : "))
num2 = int(input("Enter a num2 : "))

num1=num1+num2

num2= num1-num2
num1 = num1-num2

print(f"the num1 : {num1}")
print(f"the num2 : {num2}")