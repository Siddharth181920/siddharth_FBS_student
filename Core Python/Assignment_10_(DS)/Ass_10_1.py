# WAP to find sum of all elements of list.


li = [2,1,3,4,5,6,7,18,9,20]

sum = 0

for i in range(0,len(li)):
    print(li[i],end=" ")

    sum +=li[i]

print(f"\nThe sum of total list Number is :{sum}")


