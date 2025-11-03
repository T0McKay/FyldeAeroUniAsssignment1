from inventory_database_classDec import InventoryDatabase
from user_classDec import User
import sys

class SystemClass:
    invDatabase = InventoryDatabase()

    def __init__(self):
        User.initialiseListOfUsers()
        self.login()

    def login(self):
        i = 0
        while i != 3 :
            inputID = input("Enter employee ID : ")
            inputPassword = input("Enter password    : ")
            if User.validateUser(inputID, inputPassword):
                print("Login Successful")
                print("")
                self.menu()
            else:
                print("Username or password incorrect")
                print("")
                i = i + 1
        #login has been attempted 3 times and failed - for safety system is shut down
        print("Login failed too many times. System Shutting Down.")
        exit() #quits program

    def menu(self):
        print("-----------------------------------")
        print("--- FYLDE AERO INVENTORY SYSTEM ---")
        print("-----------------------------------")
        print("")
        print("Please select an option:")
        print("1 - View Items")
        print("2 - Add Item")
        print("3 - Remove Item")
        print("4 - Add User")
        print("5 - Log out")
        print("")
        choice = input("Input: ")
        #as a specific range is needed, checking input is an option 1-5 must also be done
        while not (choice.isdigit() and 0 < int(choice) < 6):
            choice = input("Invalid, please re-enter: ")
        choice = int(choice) #for int condition checking

        if choice == 1: #view or search
            self.invDatabase.viewItems()
        elif choice == 2: # add
            self.invDatabase.addItem()
        elif choice == 3: #remove
            self.invDatabase.removeItem()
        elif choice == 4: #log out
            User.addUserByInput()
        elif choice == 5:
            # saves everything to file
            sys.exit(0)  # exits program

        input("Press any key to continue...")
        self.menu()

