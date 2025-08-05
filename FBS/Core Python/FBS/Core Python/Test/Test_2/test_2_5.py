#A man goes for shoping . He buys 5 products. accept the price of all products display 
# the total bill after adding 18% GST .

pr_price_1 = int(input("Enter the price of product 1 :"))
pr_price_2 = int(input("Enter the price of product 2 :"))
pr_price_3 = int(input("Enter the price of product 3 :"))
pr_price_4 = int(input("Enter the price of product 4 :"))
pr_price_5 = int(input("Enter the price of product 5 :"))



total_price= pr_price_1+pr_price_2+pr_price_3+pr_price_4+pr_price_5
gst= (total_price*18)/100

total_bill = total_price+gst
print(f"The price of product 1 with gst : {total_bill}")

