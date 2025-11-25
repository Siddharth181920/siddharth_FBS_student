from prettytable import PrettyTable
from asset import AssetD

class Addasset():

    def __init__(self):

        print('''\n\033[1;38;05;208m========== ADD ASSET ==========\033[0m \n''')
      

        id = input("Asset ID :")
        name = input("Name :")
        type = input("Type :")
        status = input("Status :")
        quantity = input("Quantity :")

        a1 = AssetD(id,name,type,status,quantity)
        
        stock = str(a1)

        with open("inventoryInfoData.txt",'a') as fp:
            fp.write(stock+'\n')
        
        print('Added Asset :',stock)
        # print(stock)

        
        print("\n\033[1;33mAsset Added Successfully...!\033[0m\n")

        
        




# if(__name__ == "__main__"):
#     d1 = Addasset()

    
        
        