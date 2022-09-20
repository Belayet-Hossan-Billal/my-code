class User:
    name = ""
    email = ""
    password = ""
    login = False

    def login(self):
        email = input("Enter email: ")
        password = input("Enter password: ")

        if email == self.email and password == self.password:
            login = True
            print("login Successfull!")
        else:
            print("login faild!")

    def logout(self):
        login = False
        print("log out!")
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
user1 = User()

user1.name = "Belayet Hossan"
user1.email = "Belayethossan492@gmail.com"
user1.password = "0141516"

user1.login()