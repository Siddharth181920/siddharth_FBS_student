# WAP to find Minimum and maximum number in the given list.


li = [10,40,94,50,84]

max = li[0]
min = li[0]

for i in range(0,len(li)):
    # print(li[i])n
    if(li[i]>=max):

        max=li[i]
print(f"The maximum number is :{max}")

   
for i in range(0,len(li)):

    if(li[i]<=min):

        min = li[i]
print(f"The minimum number is :{min}")