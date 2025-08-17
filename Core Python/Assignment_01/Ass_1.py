#WAP to calculate the percentage of student based on marks on 5 subjects.

marathi = int(input('Enter the marks of marathi : '))

hindi = int(input('Enter the marks of hindi : '))

english = int(input('Enter the marks of english : '))

science = int(input('Enter the marks of science :'))

math = int(input('Enter the marks of math : '))


total_m = marathi + hindi + english + science + math

per = (total_m/5*100)



print(f"The percentage of student is : { per}%")