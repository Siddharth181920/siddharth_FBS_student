num = int (input("Enter a number : "))


if (num>0):
    if(num>10):
        if(num>50):
            if(num>100):
                if(num>150):
                    if(num>200):
                        if(num>250):
                            print("Number is greater than 250")
                        else:
                            print("Number is 250 or less than 200 ")
                    else:
                        print("Number is Greater than 150 or less 200")
                else :
                    print("Number is greater than 100 or less than 150")
            else :
                print("Number is greater than 50 or less than 100")
        else :
            print("Number is greater than 10 or less than 50")
    else :
        print("Number is Greater than 0 or less than 10")
    
else :
    print("It is less than OR 0")