# WAP to enter P(principle amt),T(time),R(Rate) and calculate simple interest. 
 
p = int( input("Enter the value of P : "))
t = int(input("Enter the value of T : "))
r = int( input("Enter the value of R : "))


simple_interest= p*t*r/100

print(f"The simple interest is : {simple_interest}")