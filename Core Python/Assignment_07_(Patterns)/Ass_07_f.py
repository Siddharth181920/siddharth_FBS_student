# WAP to print the following pattern


''''
1 2 3 4 5 
  2     5 
    3   5
      4 5
        5

       '''

n = 5

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == 1 or j == i or j == n:
            print(j, end=" ")
        else:
            print(" ", end=" ")
    print()