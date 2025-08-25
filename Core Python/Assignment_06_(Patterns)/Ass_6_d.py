# WAP to print ABCD in the follwing format 
'''
A
A B       
A B C
A B C D
A B C D E '''

for i in range(1,6):
    for j in range(1,6):
        
        if(j<=i):
            print(chr(64+j),end=" ")


        else:
            print(' ',end=" ")

    print()