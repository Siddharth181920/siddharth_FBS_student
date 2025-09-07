# Python program to sort a list according to the length of the elements within the list.

fruit = ['lemon','Potato','Guva','oh','a']


for i in range(1,len(fruit)):
    for j in range(0,len(fruit)-i):

        if(len(fruit[j])>len(fruit[j+1])):
            
            fruit[j],fruit[j+1]=fruit[j+1],fruit[j]


print(fruit)