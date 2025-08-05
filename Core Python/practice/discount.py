#find the price of item when discount is given (specify different discount based on price.)

price= int(input("Enter the price of product : "))

if(price>=5000):
    dis = (price*5)/100
    fi_Price = price-dis
    print(f"The price is greater than 5000 : {fi_Price}")

    if(price>=10000):
        dis1 = (price*10)/100
        fi_Price1= price-dis1
        print(f"The price is above 10000 : {fi_Price1}")

    if(price>=15000):
        dis2= (price*15)/100
        fi_Price2=price-dis2
        print(f"The price of greater than 15000 : {fi_Price2}")

else:
    print(f"Enter the correct value according to condition.")