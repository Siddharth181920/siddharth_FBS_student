# WAP to put even and odd elements in two different list.


def evenOdd(numbers):

    numbers = [1,2,3,4,5,6,7,8,9,10]

    even_num = [i for i in numbers if i%2==0 ]

    print(even_num)

    odd = [i for i in numbers if i % 2 !=0]

    print(odd)

numbers = input("Enter a number :")
num = list(map(int, numbers.split()))

print(num)
evenOdd(numbers)