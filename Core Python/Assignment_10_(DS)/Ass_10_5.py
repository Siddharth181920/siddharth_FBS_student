# Accept the number from user and check if this element is 
# present in the list or not.also tell how many times it present in the list.

list = [1,2,3,2,3,4,2,3,4,6,3,4,2,7]

check = 15

# print(list.count(check))
if check in list:
    print(list.count(check))
else:
    print(False)

