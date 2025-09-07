# # Python program to merge two list and sort it.


num1 = [18,54,25,87,22,118]
num2 = [29,35,88,119,22,13,120]

merge = num1+num2

print(f"Without sorted list :{merge}")

for i in range(1,len(merge)):
    for j in range(0,len(merge)-i):

        if(merge[j]>merge[j+1]):
            merge[j],merge[j+1]=merge[j+1],merge[j]

            print(merge)
            
print(f"The Sorted list : {merge}")