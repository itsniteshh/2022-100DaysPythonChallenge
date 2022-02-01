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

user1 = User("Nitesh", "Jha", "itsnitesh", "niteshjhasays@gmail.com")
user1.describe_user()
user1.greet_user()