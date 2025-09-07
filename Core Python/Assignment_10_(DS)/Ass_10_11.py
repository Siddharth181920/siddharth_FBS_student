# WAP to print all numbers which are divisible by m and n in the list.

li = [1,2,3,4,5,6,7,8,9,10,11,12,14]

result = []
m = int(input("Enter m value :"))
n = int(input("Enter n value :"))

for i in range(0,len(li)):
    if(i%m!=0 and i%n!=0):
        result.append(li[i])
    
print(result)