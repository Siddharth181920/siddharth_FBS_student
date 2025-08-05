#WAP to accept year from user and check if it is a leap year or not.

year = int(input("Enter the yea : "))

if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print(f"Leap year")
        else:
            print(f"Not leap year")
    else:
        print(f"Leap Year")
else:
    print(f"Not a leap year.")