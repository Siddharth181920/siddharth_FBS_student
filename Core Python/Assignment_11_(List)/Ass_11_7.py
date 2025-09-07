# Python program to find the intersection in two list .


list1 = [18,19,20,23,4,3]
list2 = [13,42,18,19,20,53]

intersection = list(set(list1) & set(list2))


print(intersection)