# Python program to concatenate two dictionaries into one.

dict = {'Name': 'Siddheshwar Thaware', 'Age': 22, 'DoB':'05_Oct_2003'}

dict_1 = {'Class':'MSC.FY'}
dict_2 = {'Weight':'57kg'}

dict.update(dict_1)
dict.update(dict_2)

print(dict)