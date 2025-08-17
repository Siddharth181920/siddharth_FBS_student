#  WAP to print following pattern 


''' 
1               1 
1 2           2 1 
1 2 3       3 2 1 
1 2 3 4   4 3 2 1 
1 2 3 4 5 4 3 2 1 
   '''

n = 5

for i in range(1, n + 1):
   
    for j in range(1, i + 1):
        print(j, end=" ")

   
    spaces = (n - i) * 2
    for s in range(spaces):
        print(" ", end=" ")

    
    if i != n:
        for j in range(i, 0, -1):
            print(j, end=" ")
    else:
        for j in range(i - 1, 0, -1):  
            print(j, end=" ")

    print()