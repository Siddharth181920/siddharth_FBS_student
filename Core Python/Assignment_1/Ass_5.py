#WAP to enter P(principle amt), T(time), and R(rate) and calculate compund interest.

p = int(input("Enter a value of P : "))
t = int(input("Enter a value of T : "))
r = int(input("Enter a value of R : "))

compund_interest = p*1+r*t

print(f"This is the compound interest : {compund_interest}")