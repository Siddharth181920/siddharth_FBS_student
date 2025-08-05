#WAP to calculate total salary of employee based on basic da = 10% of basic , 
#ta= 12% of basic, hra = 15% of basic.

salary = int(input("Enter the employee salary : "))

da = salary/10
ta = salary/12
hra = salary/15

to_salary= salary+da+ta+hra

print(f"The total Gross salary is : {to_salary}")

