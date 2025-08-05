#WAP to convert days into years , weeks and days.

days = int(input("Enter the days to convert years,weeks,days. : "))

years = days//365
day= days%365

week = day//7
d1= day%7



print(f"Years : {years}, Weeks : {week} and Days : {d1}")
