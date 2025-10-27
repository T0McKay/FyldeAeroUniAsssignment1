import csv, os

class User:
    ListOfUsers = {}

    #initialises a user with an ID
    def __init__(self, userID, password):
        self.userID = userID
        self.password = password
        User.ListOfUsers[userID] = self #adding self to inventory instead of password for encapsulation

    #due to encapsulation, password can only be accessed through this method
    #makes password protection slightly safer
    def validatePassword(self, queriedPassword):
        if queriedPassword == self.password:
            return True
        else:
            return False

    #used at start of program to get all known users out of CSV to be used in runtime
    @classmethod
    def initialiseListOfUsers(cls):
        if os.path.getsize("users.csv") > 0: #makes sure csv is not empty
            #reading from CSV:
            with open("users.csv", "r", newline="") as csvfile:
                csvreader = csv.reader(csvfile, delimiter=',')
                #initialises each row as an object for use
                for row in csvreader:
                    savedUser = User(row[0], row[1])

    #allows user object to be added at runtime through user input
    @classmethod
    def addUserByInput(cls):
        print("----------------")
        print("--- ADD USER ---")
        print("----------------")
        print("")
        userID = input("Enter new user ID: ")
        password = input("Enter new user password: ")
        newUser =User(userID, password)
        with open("users.csv", "a", newline="") as csvfile:
            writingToFile = csv.writer(csvfile)
            writingToFile.writerow(newUser.__dict__.values()) #tranforms object into dictionary for writing to CSV
        print("")
        print("User added successfully")
        print("")

    #used to log in - checks userID and returns true if matches parameter
    @classmethod # this function belongs to the class not an individual user object
    def validateUser(cls, queriedUserID, queriedPassword):
        #loops through known users to check if the ID entered is one
        for i in User.ListOfUsers:
            if i == queriedUserID:
                x = cls.ListOfUsers.get(queriedUserID)
                if x.validatePassword(queriedPassword):
                    return True #existing user
        #has exited loop so not a known user ID
        return False
