#WAP to prompt user to enter user_id and password , after verifying user_id and password 
# display a four digit random number ask user to enter the same number. if user enter the 
# same number then show him succes message otherwise faild.(Something like captcha)

#import random
#captcha = random.randint(1111, 9999)
#print(captcha)


user_id = (input(f"Enter the user_id of User for log-in :"))
pass_word = int (input("Enter the Password of user_id : "))


if(user_id == 'admin' or pass_word == '1234'):

    print(f"User_id and Pass_word is correct ")
    import random

    captcha = random.randint(1111, 9999)

    print(captcha)

else : 
    print(f"Plese enter the correct id and password.")
    

