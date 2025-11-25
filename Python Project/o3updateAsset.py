class UpdateAseet():

    def __init__(self):

        print('''\n\033[1;38;05;208m========== UPDATE ASSET ==========\033[0m \n''')
      
        asset_id_to_update = input("Enter Asset ID to update: ")

    
        with open("inventoryInfoData.txt",'r') as fp:
                lines = fp.readlines()

        updated_lines = []
        found = False

        for line in lines:
                line = line.strip()
                data = line.split(',')

                if data[0] == asset_id_to_update:
                    found = True
                    print("Current Asset Data:", line)
                    data[1] = input("New Name: ")
                    data[2] = input("New Type: ")
                    data[3] = input("New Status: ")
                    data[4] = input("New Quantity: ")
                    line = ','.join(data)

                updated_lines.append(line)

        if not found:
                print("\033[1;31mAsset ID not found...!\033[0m\n")
                return

        with open("inventoryInfoData.txt", 'w') as fp:
                for line in updated_lines:
                    fp.write(line + '\n')

        print("\n\033[1;33mAsset Updated Successfully...!\033[0m\n")
       
      


        

# if(__name__ == "__main__"):
#     u1 = UpdateAseet()