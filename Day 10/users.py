class User:
    '''A real life program to store user profile'''

    def __init__(self, fname, lname, age, location, username):
        #various attributes realted to user profile
        self.fname = fname
        self.lname = lname
        self.age = age
        self.location = location
        self.username = username

    def describe_user(self):
        #method for describing user
        print(f"The user's full name is {self.fname} {self.lname}")
        print(f"The user {self.fname} is {self.age} years old")
        print(f"The user is located in {self.location}")
        print(f"The users username is {self.username}")

    def greet_user(self):
        #method for greeting user
        print(f"\nWelcome {self.username}")

user1 = User("Nitesh", "Jha", 25, "Mumbai", "nitesh_who")
user1.describe_user()
user1.greet_user()
    


    