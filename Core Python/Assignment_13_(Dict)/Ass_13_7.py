# Python program to remove given key from dictionary

kirana = {1:'Sugar',2:'Tomato',3:'Potato',4:'Carrot'}

rem = int(input("Enter a key for remove :"))

# kirana.clear() // using pop method we can easily remove the item from dictionary

print(kirana.pop(rem))
print(kirana)