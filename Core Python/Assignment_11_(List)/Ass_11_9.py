# WAP to create three list of numbers , their squares and cubes.

list1 = [1,2,3,11]
list2 = [5,6,7,8]
list3 = [9,10,11,12]


square1 = [i**2 for i in list1]
cube1 = [i**3 for i in list1]

square2 = [i**2 for i in list2]
cube2 = [i**3 for i in list2]


square3 = [i**2 for i in list3]
cube3 = [i**3 for i in list3]

print(f"Square list_1 : {square1}")
print(f"Cube list_1 : {cube1}")
print(f"Square list_2 : {square2}")
print(f"Cube list_2 : {cube2}")
print(f"Square list_3 : {square3}")
print(f"Cube list_3 : {cube3}")


# for i in list1:
#     print([i**2])