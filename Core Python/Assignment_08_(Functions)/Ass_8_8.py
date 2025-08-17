# WAP to find reverse of number 

def reverse (num):

    d1 = num//100
    d = num//10
    d2 = d%10
    d3 = num%10

    print(f"{d3}{d2}{d1}")


num = int(input(f"Enter a number for reverse :"))

reverse(num)