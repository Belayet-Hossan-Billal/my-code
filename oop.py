class User:
    name = ""
    email = ""
    password = ""
    login = False

    def login(self):
        email = input("Enter Email: ")
        password = input("Enter your Password: ")

        if email == self.email and password == self.password:
            login = True
            print("Login Successful!")
        else:
            print("Login Faild!")

    def logout(self):
        login = False
        print("Logged out!")
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

User1 = User()

User1.name = "Belayet Hossan"
User1.email = "belayet35492@gmail.com"
User1.password = "1234567890"

User1.login()






