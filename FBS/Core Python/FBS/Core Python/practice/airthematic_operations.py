'''Accept two numbers from user and operator (+,*,-,/,%) based on that perform the desired operations.'''

num1 = int(input("Enter the num1 : "))
num2 = int(input("Enter the num2 : "))

opt = str(input("Select the operator of desired operation (add(+),multi(*),substr(-),divi(/),modu(%)) :"))



if(opt == '+'):
    add = num1+num2
    print(f"Addition of {num1} and {num2} is : {add}")
elif(opt=='*'):
        multi = num1*num2
        print(f"Multiplication of {num1} and {num2} is : {multi}")
elif(opt=='-'):
        substr=num1-num2
        print(f"Substraction of {num1} and {num2} is : {substr}")
elif(opt=='/'):
    divi=num1/num2
    print(f"Division of {num1} and {num2} is : {divi} ")
elif(opt=='%'):
    modu= num1%num2
    print(f"The reminder is {num1} and {num2} is : {modu}")
else:
    print(f"Select the desired operator .")


