'''Display a menu to the user (like 1. odd , even 2. Basic salary etc) ask the user to enter his choice
, then based on that perfom the desired operations.'''


choice= str(input("Select your choice(1 or 2) \n1. Even/odd \n2. Basic salary \n:- "))

if(choice=='1'):
    num=int(input("Enter the number to check if even or odd : "))
     
    if(num/2==0):
       print(f"It is even number .")
    else:
        print(f"It is odd number.")

elif(choice=='2'):
    basic= int(input("Enter the basic salary to calculate : "))

    da=basic/10
    ta=basic/20
    hra=basic/25

    salary= basic+da+ta+hra

    print(f"Your Total salary is :{salary}")

else:
    print(f"Select a desired and correct option repeat.")