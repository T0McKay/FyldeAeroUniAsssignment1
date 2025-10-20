from datetime import datetime, date

class InventoryItem:
    # declares attributes
    name: str
    productCode: int
    expiryDate: date
    quantity: int
    location: str

    #initialises new inventory item
    def __init__ (self):
        #declares each attribute with validation functions
        inputName = input("Name         : ")
        self.name = self.validStrInput(inputName)
        inputProductCode = input("Product code : ")
        self.productCode = self.validIntInput(inputProductCode)
        inputExpiryDate = input("Expiry Date  : ")
        self.expiryDate = self.validExpiryDate(inputExpiryDate)
        inputQuantity = input("Quantity     : ")
        self.quantity = self.validIntInput(inputQuantity)
        inputLocation = input("Location     : ")
        self.location = self.validStrInput(inputLocation)

    #displays an items defined attributes
    def displayItem(self):
        print(f"Product code : {self.productCode}")
        print(f"Name         : {self.name}")
        print(f"Expiry Date  : {self.expiryDate.strftime('%m/%d/%Y')}")
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