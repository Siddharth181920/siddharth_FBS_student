'''WAP to find greatest of three numbers using nested if-else.'''

num1= int(input("Enter the num1 :"))
num2= int(input("Enter the num2 :"))
num3= int(input("Enter the num3 :"))

if(num1>num2):
    
    if(num1>num3):
            print(f"Num1 is greatest.")
    else :
        print(f"Num3 is greatest")

    
else :
 if(num2>num3):
    print(f"Num2 is greatest .")
 else:
     print(f"Num3 is greatest.")