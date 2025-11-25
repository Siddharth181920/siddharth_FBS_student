from o1addAsset import Addasset
from o2viewInventory import ViewInventory
from o3updateAsset import UpdateAseet
from o4searchAsset import SearchAseet
from o5removeAsset import RemoveAseet

class inventory():

    def login():
        # print("Perform this operation to manage Asset.")

        print(''' \n\033[1;38;05;208m========== ASSET MANAGEMENT SYSTEM ==========\033[0m
            
            
            1. Add Asset
            2. View Inventory
            3. Update Asset Status
            4. Search Asset    
            5. Remove Asset            
            6. Save & Exit
              ''')
        ch = 0
        while(ch !='6'):
            ch = input("Enter a choice num which you want to perform operation :")
            
            if(ch == '1'):
                Addasset()
            elif(ch=='2'):
                ViewInventory()
            elif(ch=='3'):
                UpdateAseet()
            elif(ch=='4'):
                SearchAseet()
            elif(ch=='5'):
                RemoveAseet()
            elif(ch=='6'):
                print("\n\033[1;33mSaved & Exist...!\033[0m")
            else:
                print("Enter a Valid Choice for perform appropriate operation.")


if(__name__ == "__Main__"):

    log1 = inventory()
    log1.login()