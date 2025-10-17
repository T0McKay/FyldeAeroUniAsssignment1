class User:
    ListOfUsers = ["tm123","ts67"]

    #initialises a user with an ID
    def __init__(self, userID):
        self.userID = userID

    #used to log in - checks userID and returns true if matches parameter
    @classmethod # this function belongs to the class not an individual user object
    def verifyIfUser(cls, queriedUserID):
        #loops through known users to check if the ID entered is one
        for i in User.ListOfUsers:
            if i == queriedUserID:
                return True
        #has exited loop so not a known user ID
        return False
