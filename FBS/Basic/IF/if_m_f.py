gen = (input("Enter the Gender (M/F) : "))

age = int (input("Enter the Age :"))


if((gen=='M' and age>=21 ) or (gen == 'F' and age>=18 )):

    print("You are eligible for marriage .")
else :
    print("You are not eligible of marriae .")
