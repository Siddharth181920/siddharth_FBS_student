# WAP to print create three list of numbers their squares and cubes.

li_1 = input("Enter number for list_1 : ")
li_2 = input("Enter number for list_2 : ")
li_3 = input("Enter number for list_3 :")



num_1 = list(map(int,li_1.split()))
num_2 = list(map(int,li_2.split()))
num_3 = list(map(int,li_3.split()))

squares_1 = [num**2 for num in num_1]
squares_2 = [num**2 for num in num_2]
squares_3 = [num**2 for num in num_3]

print(f"The squares of list_1 :{squares_1}")
print(f"The squares of list_2 :{squares_2}")
print(f"The squares of list_3 :{squares_3}")


cubes_1 = [num**3 for num in num_1]
cubes_2 = [num**3 for num in num_2]
cubes_3 = [num**3 for num in num_3]


print(f"The cubes of list_1 :{cubes_1}")
print(f"The cubes of list_2 :{cubes_2}")
print(f"The cubes of list_3 :{cubes_3}")
