# Python program to sort the list according to the second element in sublist.


list = [[1,19],[4,18],[6,20],[3,118],[8,119]]

for i in range(1,len(list)):
    for j in range(0,len(list)-i):

        if(list[j][1]>list[j+1][1]):
            list[j][1],list[j+1][1]=list[j+1][1],list[j][1]

print(f"Sorted sub list : {list}")