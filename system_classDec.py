from user_classDec import User

class SystemClass:

    def __init__(self, password):
        self.password = password

    def login(self):
        i = 0
        while i != 3 :
            inputID = input("Enter employee ID : ")
            inputPassword = input("Enter password    : ")

            if User.verifyIfUser(inputID) and inputPassword == self.password:
                print("Login Successful")
                return True #information will then be read from csv and database initialised in program
            else:
                print("Username or password incorrect")
                i = i + 1
        #login has been attempted 3 times and failed - for safety system is shut down
        print("Login failed too many times. System Shutting Down.")
        exit()
