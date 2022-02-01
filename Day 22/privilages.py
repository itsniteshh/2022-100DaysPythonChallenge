class Privilages():
    """A real life example to show privilage of an admin"""
    
    def __init__(self, privilage):
        self.privilage = privilage = ["can post", "can delete post", "can add user", "can make changes to the page"]

    def show_privilages(self):
        #a method to show the work of admin
        print(f"The adming can: ")
        for privilages in self.privilage:
            print(privilages)

    