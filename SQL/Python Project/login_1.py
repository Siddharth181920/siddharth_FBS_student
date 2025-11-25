from main_2 import inventory
import getpass


print('''\n\033[1;38;05;208m========== ASSET MANAGEMENT SYSTEM ==========\033[0m
      
                LOG-IN
      ''')

user = 'admin' 
passw = '2025'

while True:
    
    user = input("\033[0;35mUser-ID  :\033[0m")
    passw = getpass.getpass("\033[0;35mPassword :\033[0m")

    if(user == 'admin' and passw == '2025'):

        break
    else:
        print("Invalid Password Try Again!")

print("\n\033[1;33mLog-In SuccessFully.\033[0m")
inventory.login()


