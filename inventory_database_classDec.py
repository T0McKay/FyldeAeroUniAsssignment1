from inventory_item_classDec import InventoryItem

class InventoryDatabase:

    #initialises object
    def __init__ (self):
        self.ListOfItems = []

    #adds item to list
    def addItem (self, item):
        self.ListOfItems.append(item)
        print("Item added successfully")

    #prints out all items + related details in the list
    def viewItems(self):
        indexCount = 0
        if self.ListOfItems.__len__() == 0: #if list is empty then there's no items
            print("No items in inventory database")
        else:
            for i in self.ListOfItems: #loops through every index in the list
                indexCount += 1
                print(f"Item Number  : {indexCount}")
                i.displayItem()

    #removes requested item (parameter) from the list
    def removeItem (self, item):
        self.ListOfItems.remove(item)
        print("Item removed.")

    
