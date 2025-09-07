# WAP to print list after removing even numbers 


list = [1,2,3,4,5,6,7,8,9,10]

odd = [i for i in list if i%2!=0]
print(f"The list is after removing even number :{odd}")