#WAP to prompt user to enter userid and password . If ID and Password 
# is incorrect give him chance to re-enter the credentials 
#Let him try 3 times , after that program to terminate .

user_id = (input("Enter a user id (admin): "))

pass_word = int(input("Enter a Pass (1234): "))


if(user_id == 'admin' and pass_word == '1234' ):

    print(f"Your name is correct.")
else:

    print(f"Plese try again ")
