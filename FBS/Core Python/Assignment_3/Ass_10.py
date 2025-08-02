#WAP to check if person is eligible to marry or not (male age >= 21 or female age >=18)

gen = (input("Enter the Gender (M/F):"))
age =  int(input("Enter the age : "))

#if((gen=='M'and age>=21) or (gen=='F' and age>=18)):
if((gen=='M' and age>=21 ) or (gen == 'F' and age>=18 )):
    print(f"You are eligible for marry .")
else :
    print(f"Plese, Wait...")


    