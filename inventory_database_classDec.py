from inventory_item_classDec import InventoryItem

class InventoryDatabase:
    ListOfItems = []

    #initialises object
    def __init__ (self):
        #becomes initialised w csv file
        ListOfItems = []

    #adds item to list
    def addItem (self):
        print("--------------------------")
        print("--- NEW INVENTORY ITEM ---")
        print("--------------------------")
        print("")
        item = InventoryItem()
        self.ListOfItems.append(item)
        print("")
        print("Item added successfully")

    #prints out all items + related details in the list
    def viewItems(self):
        print("---------------------------")
        print("--- INVENTORY ITEM LIST ---")
        print("---------------------------")
        print("")
        indexCount = 0
        if self.ListOfItems.__len__() == 0: #if list is empty then there's no items
            print("No items in inventory database")
        else:
            for i in self.ListOfItems: #loops through every index in the list
                i.displayItem()
                print("")

    #removes requested item (parameter) from the list ----- NEEDS TO BE FIXED
    def removeItem (self):
        print("-------------------------------")
        print("--- REMOVING INVENTORY ITEM ---")
        print("-------------------------------")
        print("")
        searchedProdCode = input("Please enter the PRODUCT CODE of the item you want to remove: ")
        print("")
        found = False
        for item in self.ListOfItems:  # loops through every item in the list
            if item.productCode == searchedProdCode:
                found = True
                #should probably make choice to confirm it is the right item
                print("Please confirm this is the item you would like to delete:")
                item.displayItem()
                confirmation = input("Enter 1 for Yes or 0 for No: ")
                while not (confirmation.isdigit() and 0 <= int(confirmation) <= 1):
                    confirmation = input("Invalid, please re-enter: ")

                if int(confirmation) == 1:
                    self.ListOfItems.remove(item)
                    print("Item removed successfully")
                    break #exits the for loop so program does not loop through rest of list
        if not found:
            print("Item not found")

    
