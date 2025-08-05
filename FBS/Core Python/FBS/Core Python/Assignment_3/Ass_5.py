#WAP for to check whether the triangle is equilateral , isosceles or scalene triangle.

# equi a==b==b==c / (a==b)and (b==c)and(c==a)
# iso two side are same in any
#scalene   all sides and angles are not equal 

side1 = int(input("Enter the side 1 : "))
side2 = int (input("Enter the side 2 :"))
side3 = int(input("Enter the side 3 : "))

a = side1
b = side2
c = side3

if(a==b==b==c):
    print(f"it is equilateral triangle")

elif (side1==side2 or side2==side3 or side3==side1 ):

    print(f"It is Isosceles triangle")

elif (side1!=side2 or side2!=side3 or side3!=side1 ) :

    print(f"Scalene triangle")

else :
    print(f"Provide a correct value for checking triangle .")
