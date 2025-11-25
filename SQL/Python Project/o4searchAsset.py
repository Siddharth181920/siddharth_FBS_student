
from prettytable import PrettyTable
class SearchAseet():

#     # def __init__(self):

#     #     print('''\n\033[1;38;05;208m========== SEARCH ASSET ==========\033[0m \n''')
      
            


    def __init__(self):
        print('''\n\033[1;38;05;208m========== SEARCH ASSET ==========\033[0m \n''')
        asset_id = input("Enter Asset ID to search: ")
        self.search_by_id(asset_id)

    def search_by_id(self, asset_id):

        try:
            with open("inventoryInfoData.txt", "r") as file:
                for line in file:
                    data = line.strip().split(",")  # Split saved asset data

                    if data[0] == asset_id:        # Check ID match
                        table = PrettyTable(["Asset ID", "Name", "Type", "Status", "Quantity"])
                        table.add_row(data)

                        print("\nAsset Found:\n")
                        print(table)
                        print("\n\033[1;33mSearch Asset Successfully...!\033[0m\n")

                        return
        except FileNotFoundError:
            print("Error: inventoryInfoData.txt not found!")
            return

        print("\nAsset not found.")
        
       

if(__name__ == "__main__"):
    s1 = SearchAseet()




