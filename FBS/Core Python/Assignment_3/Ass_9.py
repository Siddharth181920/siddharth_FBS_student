#Input 5 Subje ts marks from user and display grade(eg.First class, Second Class , Third Class..) 


sub1 = int(input("Enter the sub1 marks :"))
sub2 = int(input("Enter the sub2 marks :"))
sub3 = int (input("Enter the sub3 marks :"))
sub4 = int(input("Enter the sub4 marks : "))
sub5 = int(input("Enter the sub5 marks :"))


total_marks= sub1+sub2+sub3+sub4+sub5

per = total_marks/500*100


if(per>=90):
    print(f"It is above {per} First  class")
elif(per>=75):
    print(f"It is percentage above {per} Seond Class")
else :
    print(f"It is percentage lower than 75 % third class")



print(f"Your Percentage is {per}.")