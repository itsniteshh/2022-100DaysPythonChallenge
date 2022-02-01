from urllib.parse import uses_relative


class User:
    """Real life program to store users profile including name and other details"""

    def __init__(self, fname, lname, username, email_id):
        self.fname = fname
        self.lname = lname
        self.username = username
        self.email_id = email_id
        self.login_attempts = login_attempts = 0

    
    def describe_user(self):
        #method to describe user profile and details
        print(f"Current user's username is: {self.username}")
        print(f"User {self.username}'s full name is: {self.fname} {self.lname}")
        print(f"{self.username}'s email address is: {self.email_id}\n")

    def greet_user(self):
        #method to greet user
        print(f"Welcome to our page {self.username}")

    def read_login_attempts(self):
        print(f"\nYou have already tried to login {self.login_attempts} times")

    def increment_login(self):
        #fnc to increment login attempts
        self.login_attempts += 1

    def reset_login(self):
        #func to reset the value of login to zero
        self.login_attempts = 0
    

user1 = User("Nitesh", "Jha", "itsnitesh", "niteshjhasays@gmail.com")
user1.describe_user()
user1.greet_user()
user1.increment_login()
user1.increment_login()
user1.increment_login()
user1.read_login_attempts()

user1.reset_login()
user1.read_login_attempts()
