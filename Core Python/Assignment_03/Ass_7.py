#
#get user id and pass from user after getting it is need to match each other pass and user id
# if (u_id=='admin' and passw==1234)

u_id = (input("Enter the user_id : "))
pass_word =  (input("Enter the password : "))


if(u_id =='admin' and pass_word=='1234'):
    print(f"It is user_id and password is correct.")
else :
    print(f"Enter the correct user_id and Password ")