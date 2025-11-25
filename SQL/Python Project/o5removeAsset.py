class RemoveAseet():

    def __init__(self):

        print('''\n\033[1;38;05;208m========== REMOVE/DELETE ASSET ==========\033[0m \n''')


        asset_id = input("Enter Asset ID to delete: ")
        self.delete_by_id(asset_id)


    def delete_by_id(self, asset_id):

     
            with open("inventoryInfoData.txt", "r") as file:
                lines = file.readlines()

            found = False
            with open("inventoryInfoData.txt", "w") as file:
                for line in lines:
                    data = line.strip().split(",")

                    # Keep all lines except the one with matching ID
                    if data[0] != asset_id:
                        file.write(line)
                    else:
                        found = True

            if found:
                print(f"\n\033[1;33m'{asset_id}' ID Removed Asset Successfully...!\033[0m\n")
            else:
                print(f"\nAsset with ID '{asset_id}' not found.\n")

      
           


# if(__name__ == "__main__"):
#     r1 = RemoveAseet()