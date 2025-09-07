# Python program to multiply all the items in a dictionary

num = {1:2,2:2,3:3}

multiply = 1


for i in num:

    multiply = multiply*num[i]

print(f"The multiplication of all items : {multiply}")