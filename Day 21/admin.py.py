from pygame import init


class User:
    """Real life program to store users profile including name and other details"""

    def __init__(self, fname, lname, username, email_id):
        self.fname = fname
        self.lname = lname
        self.username = username
        self.email_id = email_id

    
    def describe_user(self):
        #method to describe user profile and details
        print(f"Current user's username is: {self.username}")
        print(f"User {self.username}'s full name is: {self.fname} {self.lname}")
        print(f"{self.username}'s email address is: {self.email_id}\n")


    def greet_user(self):
        #method to greet user
        print(f"Welcome to our page {self.username}")



class Admin(User):
    """A real life program to show or give the power to admin of the page"""
    def __init__(self, fname, lname, username, email_id):
        super().__init__(fname, lname, username, email_id)
        self.privilage = privilage = ["can post", "can delete post", "can add user", "can make changes to the page"]

    
    def show_privilages(self):
        #a method to show the work of admin
        print(f"The adming can: ")
        for privilages in self.privilage:
            print(privilages)

ad = Admin("Nitesh", "Jha", "itsnitesh", "niteshjhasays@gmail.com")
ad.show_privilages()

    