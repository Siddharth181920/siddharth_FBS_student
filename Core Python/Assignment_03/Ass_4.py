#Wap to input all sides of a triangle and check whether triangle is valid or not.

side1 = int(input("Enter the side of angle a :"))
side2 = int(input("Enter the side of angle b :"))
side3 = int(input("Enter the side of angle c :"))

AB = side1+side2
BC = side1+side3
CA = side2+side3

if(AB>side1):
    print(f"AB it is valid")
elif (BC>side2):
    print(f"BC it is valid")
elif (CA>side3):
    print(f" CA It is Valid")
else :
    print(f"It is not valid")