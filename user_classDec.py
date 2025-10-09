class User:

    #initialises a user with an ID
    def __init__(self, userID):
        self.userID = userID

    #used to login - checks userID and returns true if matches parameter
    def verify(self, queriedUserID):
        if (queriedUserID == self.userID):
            return True # correct user id
        else:
            return False #incorrect