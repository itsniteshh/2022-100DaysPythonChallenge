class Restaurant:
    """A real life program to replicated Restaurants name and cuisine type"""

    def __init__(self, restro_name, cuisine_type):
        #method to initialise self and store values
        self.restro_name = restro_name
        self.cuisine_type = cuisine_type

    def describe_restro(self):
        #method to describe restro and its cuisine
        print(f"\nThe restaurant name is {self.restro_name}")
        print(f"{self.restro_name} serves {self.cuisine_type} dishes")

    
    def open_restaurant(self):
        #method to show if the restaurant is open or not
        print(f"{self.restro_name} is now open for dining and takeaways")



class IceCreamStand(Restaurant):
    """A simple program to replicate real world ice cream restro"""
    
    def __init__(self, restro_name, cuisine_type):
        super().__init__(restro_name, cuisine_type)
        self.flavors = flavors = ["Vanilla", "Chocolate", "starwberry", "butterscotch"]

    





restro = Restaurant("Hope", "chinese")
restro.describe_restro()

