#Convert the time enterd in hhh, min and sec into seconds.
Hour = int(input("Enter a Time in Hour : "))
Minutes = int (input("Enter a Time in Minutes :"))
Seconds = int (input("Enter a Time in Seconds : "))


sec1 = Hour * 3600
sec2 = Minutes* 60

Sec = sec1+sec2+Seconds

print(f"This is the converted seconds : {Sec}")



'''
time = int(input("Enter the time : "))

temp = time 
Hr = temp // 60 


Min = temp/60


#Sec = temp/60

print(f"The time is Hr {Hr}hr , Min {Min} ")'''