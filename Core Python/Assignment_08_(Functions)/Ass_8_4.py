# WAP to sum of all odd numbers between 1 to n.


def odd (num):


    n = 0

    for i in range(1, num+1):

        if (i%2!=0):
            
            print(i)

            n = n+i

    return n

num = int(input("Enter a number : "))

res = odd (num)

print(f"The sum of odd number is : {res}")