#Wap for get input form user and check the angle is 180 or not 

ang1 = int(input("Enter the angle value side 1 : "))
ang2 = int(input("Enter the angle value side 2 : "))
ang3 = int(input("Enter the angle value side 3 : "))

side = ang1+ang2+ang3

if(side==180):
    print(f" {side}% It is valid angle ")
else :
    print(f" {side}% It is not valid angle")