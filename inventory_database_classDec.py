from inventory_item_classDec import InventoryItem #to get information about item
from tabulate import tabulate
from datetime import datetime, date
import csv, os

class InventoryDatabase:
    #this is a class attribute - begins empty, only initialised after login
    ListOfItems = []

    #initialises object
    def __init__ (self):
        #gets saved items and loads them into list for use at runtime
        if os.path.getsize("inventory.csv") > 0: #makes sure csv is not empty
            with open("inventory.csv", "r", newline="") as csvfile:
                csvreader = csv.reader(csvfile, delimiter=',')
                #initialises each row as an object for use
                for row in csvreader:
                    savedAsDate = datetime.strptime(row[2], "%Y-%m-%d") #this is the automatically saved format, but undesirable
                    formattedDate = savedAsDate.strftime("%d/%m/%Y") #ensures expiry date is correct format
                    savedItem = InventoryItem(row[0],int(row[1]),formattedDate,int(row[3]),row[4]) #instantiates new object
                    InventoryDatabase.ListOfItems.append(savedItem)

    #adds item to list
    def addItem (self):
        print("--------------------------")
        print("--- NEW INVENTORY ITEM ---")
        print("--------------------------")
        print("")
        #creates item with user input and adds to known list of items for use at runtime
        item = InventoryItem.initialiseItemUsingUserInput()
        self.ListOfItems.append(item)
        #saves new item to csv:
        with open("inventory.csv", "a",newline="") as csvfile:
            writingToFile = csv.writer(csvfile)
            writingToFile.writerow(item.__dict__.values()) #.__dict__.values turns object into dictionary so attributes can be written to csv
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
            headers = ["Name", "Product Code", "Expiry Date", "Quantity", "Location"]
            tableOfItems = [item.__dict__.values() for item in self.ListOfItems]
            print(tabulate(tableOfItems, headers=headers, tablefmt="grid"))
            print("")

    #removes requested item (parameter) from the list ----- NEEDS TO BE FIXED
    def removeItem (self):
        print("-------------------------------")
        print("--- REMOVING INVENTORY ITEM ---")
        print("-------------------------------")
        print("")
        searchedProdCode = input("Please enter the PRODUCT CODE of the item you want to remove: ")
        searchedProdCode = InventoryItem.validIntInput(searchedProdCode)
        print("")
        found = False
        for item in self.ListOfItems:  # loops through every item in the list
            if item.productCode == searchedProdCode:
                found = True

                #checks correct item is about to be deleted:
                print("Please confirm this is the item you would like to delete:")
                print("")
                item.displayItem()
                confirmation = input("Enter 1 for Yes or 0 for No: ")
                while not (confirmation.isdigit() and 0 <= int(confirmation) <= 1):
                    confirmation = input("Invalid, please re-enter: ")

                #if confirmed, item deleted
                if int(confirmation) == 1:
                    #removes from list being used at runtime:
                    self.ListOfItems.remove(item)

                    #removes from csv:
                    itemsToKeep = []
                    # adds all saved items to list to overwrite EXCEPT one to be deleted
                    with open("inventory.csv", "r", newline="") as csvfile:
                        for row in csv.reader(csvfile):
                            if row[1] != searchedProdCode:
                                itemsToKeep.append(row)

                    with open ("inventory.csv", "w", newline="") as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerows(itemsToKeep)

                    print("")
                    print("Item removed successfully")
                    break #exits the for loop so program does not loop through rest of list

                #if right item, but no longer desired to be deleted, returns to menu
                elif int(confirmation) == 0:
                    input("Press any key to return to menu...")
                    break #exits the for loop so program does not loop through rest of list
        if not found:
            print("Item not found")
