from prettytable import PrettyTable

class ViewInventory():

    def __init__(self):

        print('''\n\033[1;38;05;208m========== VIEW INVENTORY ==========\033[0m \n''')
      

        asdata = PrettyTable(["ID","Name","Type","Status","Quantity"])

        with open('inventoryInfoData.txt','r') as fp:

            for line in fp:
                row = [item.strip() for item in line.split(",")]
                asdata.add_row(row)
        print()
        print(asdata)
        # fp.close()
        

        print("\n\033[1;33mSuccesfully Viewed Inventory...!\033[0m\n")

        

# if(__name__ == "__main__"):
#     v1 = ViewInventory()


















#        from prettytable import PrettyTable

# table = PrettyTable(["ID", "Name", "Age"])

# with open("data.txt", "r") as file:
#     for line in file:
#         row = [item.strip() for item in line.split(",")]
#         table.add_row(row)

# print(table)
