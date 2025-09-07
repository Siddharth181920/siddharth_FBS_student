# WAP to print list after removing even numbers.

li = [1,2,3,4,5,6,7,8,9,10]

result = []

for i in range(0,len(li)):

    if(i%2==0):
        result.append(li[i])

print(result)