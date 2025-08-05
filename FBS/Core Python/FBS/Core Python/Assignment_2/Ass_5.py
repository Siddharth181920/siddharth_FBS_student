#WAP to calculate selling price of book based on cost price and discount.

cost_price = int(input("Enter a cost price of book : "))
dis_nt = int(input("Enter the discount of per book :"))

temp = 100/dis_nt

sell_price = temp+cost_price

print(f"The selling price of book is : {sell_price}")