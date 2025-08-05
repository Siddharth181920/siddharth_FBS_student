'''WAP to accept three digit number , if first digit double of second digit
half of third digit then display "yes , you have done it " , otherwise
display "Plese try next time."'''

num = int(input("Enter three digit number : "))

d1= num//100
d= num//10
d2= d%10
d3= num%10

print(f"{d1}, {d2}, {d3}")


if(d1/2==d2 and d3/2==d1):
    print(f"Yes , you have done it ")
else:
    print(f"Plese try next time.")





