# Python program to sum of all the items in a dictionary.



num = {1: 10, 2:20,3:30,4:45}


# sum = sum(num.values())

sum = 0

for i in num:

    sum = sum+num[i]

print(f"The sum of item is :{sum}")
