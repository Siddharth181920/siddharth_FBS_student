#WAP to print * in follwing pattern format

'''
        *
      * * *       
    * * * * *     
  * * * * * * *   
* * * * * * * * * 

'''

for i in range(1,6):
    for j in range(1,6):

        if(j>=6-i):
            print('*',end=" ")
        else:
            print(' ',end=" ")

    for j in range(2,6):
        if(j<=i):
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()

