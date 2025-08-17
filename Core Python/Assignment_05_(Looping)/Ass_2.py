'''Enter number of students from user . for those many students 
many students accepts marks of 5 subjects marks from user and
calculate percentage . Display all percentage and average percentage
of students.'''

no_of_std = int(input("Enter the number of Students : "))

num = no_of_std
i = 0

while(i<num):
    sub1= int(input(f"Enter a Sub-1 marks : "))
    sub2= int(input(f"Enter a Sub-2 marks :"))
    sub3= int(input(f"Enter a Sub-3 marks :"))
    sub4= int(input(f"Enter a Sub-4 marks :"))
    sub5= int(input(f"Enter a Sub-5 marks :"))

    sub_tot= sub1+sub2+sub3+sub4+sub5

    per= (sub_tot/500)*100

    print(per)

    i +=1
