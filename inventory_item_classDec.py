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
        na = input("Name         : ")
        self.name = self.validStrInput(na)
        pC = input("Product code : ")
        self.productCode = self.validIntInput(pC)
        ex = input("Expiry Date  : ")
        self.expiryDate = self.validExpiryDate(ex)
        qu = input("Quantity     : ")
        self.quantity = self.validIntInput(qu)
        lo = input("Location     : ")
        self.location = self.validStrInput(lo)

    # used to validate name and location attributes
    def validStrInput(self, inputStr):
        # checks if name is empty string
        while inputStr.isdigit() or len(inputStr) <= 0:
            inputStr = input ("Invalid, please re-enter: ")
        return inputStr

    # used to validate product code and quantity attributes
    def validIntInput(self, inputInt):
        # checks if product code is a positive number - if not loops until it is
        while not (inputInt.isdigit() and int(inputInt) > 0):
            inputInt = input ("Invalid, please re-enter: ")
        return int(inputInt)

    def validExpiryDate(self, expiryDate):
        #checks the expiry date is correctly formatted as DD/MM/YYYY
        valid = False
        while not valid:
            try:
                expiryDate = datetime.strptime(expiryDate, "%d/%m/%Y").date() #makes a date and excludes time
                valid = True
            except ValueError:
                expiryDate = input ("Invalid expiry date, please re-enter in format DD/MM/YYYY: ")

        return expiryDate
