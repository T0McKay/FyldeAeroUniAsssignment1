from inventory_database_classDec import InventoryDatabase
from inventory_item_classDec import InventoryItem
from user_classDec import User
import os, sys

class SystemClass:
    invDatabase = InventoryDatabase()

    def __init__(self, password):
        self.password = password

    def login(self):
        i = 0
        while i != 3 :
            inputID = input("Enter employee ID : ")
            inputPassword = input("Enter password    : ")

            if User.verifyIfUser(inputID) and inputPassword == self.password:
                print("Login Successful")
                print("")
                return inputID #information will then be read from csv and database initialised in program
            else:
                print("Username or password incorrect")
                print("")
                i = i + 1
        #login has been attempted 3 times and failed - for safety system is shut down
        print("Login failed too many times. System Shutting Down.")
        exit()

    def menu(self):
        os.system("cls")
        print("-----------------------------------")
        print("--- FYLDE AERO INVENTORY SYSTEM ---")
        print("-----------------------------------")
        print("")
        print("Please select an option:")
        print("1 - View or Search Items")
        print("2 - Add Item")
        print("3 - Remove Item")
        print("4 - Log out")
        print("")
        choice = input("Input: ")
        #as a specific range is needed, checking input is an option 1-5 must also be done
        while not (choice.isdigit() and 0 < int(choice) < 5):
            choice = input("Invalid, please re-enter: ")
        choice = int(choice) #for int condition checking

        if choice == 1: #view or search
            self.invDatabase.viewItems()
        elif choice == 2: # add
            self.invDatabase.addItem()
        elif choice == 3: #remove
            self.invDatabase.removeItem()
        elif choice == 4: #log out
            #saves everything to file
            sys.exit(0) #exits program

        input("Press any key to continue...")
        self.menu()