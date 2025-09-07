# WAP to find second largest number from list.


li = [43,64,73,58,39,68,33]

max = li[0]
snd_max = li[0]


for i in range(len(li)):

    if(li[i]>=max):
        snd_max=max
        max = li[i]
    
    elif(li[i]>=snd_max):

        snd_max=li[i]

print(f"The first maximum number is :{max}")
print(f"The second maximum number is :{snd_max}")