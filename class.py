class user:
    name = ""
    email = ""
    password = ""
    login = False

    def login(self):
        email = input("Enter email: ")
        password = input("Enter password: ")

        if email == self.email and password == self.password:
            login = True
            print("login successful!")
        else:
            print("login Faild!")

    def logout(self):
        login = False
        print("logged out!")

    def isloggedin(self):
        if self.login:
            return True
        else:
            return False
    def profile(self):
        if self.isloggedin():
            print(self.name,"\n",self.email)
        else:
            print("user is not logged in!")

user1 = user()

user1.name = "Belayet Hossan"
user1.email = "Balaet35-492@diu.edu.bd"
user1.password = "12345678*"

user1.login()
user1.profile()







