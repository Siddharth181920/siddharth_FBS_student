#Convert distant given in feet and inches into metre and centimeter.

f_dist = int(input("Enter the distance in feet : "))
I_dist = int (input("Enter the distance in inches : "))


meter = f_dist*0.3040
ce_mtr = I_dist*2.54

print(f"the {f_dist} feet is {meter} Meter")
print(f"the {I_dist} inches is {ce_mtr} centimetre")
