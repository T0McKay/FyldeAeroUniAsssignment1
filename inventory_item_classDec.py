from datetime import datetime

class InventoryItem:

    #initialises new inventory item
    def __init__ (self,name,productCode,expiryDate,quantity,location):
        self.name = name
        self.productCode = productCode
        self.expiryDate = expiryDate
        self.quantity = quantity
        self.location = location

    #displays an items defined attributes
    def displayItem(self):
        print(f"Product code : {self.productCode}")
        print(f"Name         : {self.name}")
        print(f"Expiry Date  : {self.expiryDate}")
        print(f"Quantity     : {self.quantity}")
        print(f"Location     : {self.location}")

#the following are class methods used for validation:

    # used to validate name and location attributes
    @classmethod
    def validStrInput(cls, inputStr):
        # checks if name is empty string
        while inputStr.isdigit() or len(inputStr) <= 0:
            inputStr = input ("Invalid, please re-enter: ")
        return inputStr

    # used to validate product code and quantity attributes
    @classmethod
    def validIntInput(cls, inputInt):
        # checks if product code is a positive number - if not loops until it is
        while not (inputInt.isdigit() and int(inputInt) > 0):
            inputInt = input ("Invalid, please re-enter: ")
        return int(inputInt)

    @classmethod
    def validExpiryDate(cls, expiryDate):
        #checks the expiry date is correctly formatted as DD/MM/YYYY
        valid = False
        while not valid:
            #to make sure it's in date format, program has to try the format - if it doesn't work then invalid message is output
            try:
                expiryDate = datetime.strptime(expiryDate, "%d/%m/%Y").date() #makes a date and excludes time
                valid = True
            except ValueError:
                expiryDate = input ("Invalid expiry date, please re-enter in format DD/MM/YYYY: ")
        return expiryDate

    #this method is used when the attributes need to be chosen by the user
    @classmethod
    def initialiseItemUsingUserInput(cls):
        # declares each attribute with validation functions
        inputName = input("Name         : ")
        inputName = cls.validStrInput(inputName)
        inputProductCode = input("Product code : ")
        inputProductCode = cls.validIntInput(inputProductCode)
        inputExpiryDate = input("Expiry Date  : ")
        inputExpiryDate = cls.validExpiryDate(inputExpiryDate)
        inputQuantity = input("Quantity     : ")
        inputQuantity = cls.validIntInput(inputQuantity)
        inputLocation = input("Location     : ")
        inputLocation = cls.validStrInput(inputLocation)
        # actually creates item
        newItem = InventoryItem(inputName, inputProductCode, inputExpiryDate, inputQuantity, inputLocation)
        return newItem