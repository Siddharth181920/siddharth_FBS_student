# Python program to find the union of two list.

list1 = [18,39,19,20]
list2 = [18,26,19,20]


common = list(set(list1) | set(list2))

print(common)