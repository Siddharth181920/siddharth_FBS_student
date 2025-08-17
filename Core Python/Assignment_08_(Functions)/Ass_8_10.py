# WAP to check if entered year is a leap year or not.

def leap(year):

    if(year>1000 and year%4==0):
        print(f"It is a leap year.")
    else:
        print(f"It is not a leap year.")

year = int(input("Enter a year to check leap year or not :"))
leap(year) 