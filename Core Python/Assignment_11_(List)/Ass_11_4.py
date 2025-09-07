# # Python program to find the second largest number in a list using bubble sort.


list = [18,11,4,6,3,5,19]
for i in range(1,len(list)):
    for j in range(0,len(list)-i):

        if(list[j]>list[j+1]):
            list[j],list[j+1]=list[j+1],list[j]
            
            # print(list)

print(list)
print(f"Second largest number in the list :{list[-2]}")