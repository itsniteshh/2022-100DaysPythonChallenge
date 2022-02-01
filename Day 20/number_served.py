class Restaurant:
    """A real life program to replicated Restaurants name and cuisine type"""

    def __init__(self, restro_name, cuisine_type):
        #method to initialise self and store values
        self.restro_name = restro_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served = 0

    def describe_restro(self):
        #method to describe restro and its cuisine
        print(f"\nThe restaurant name is {self.restro_name}")
        print(f"{self.restro_name} serves {self.cuisine_type} dishes")

    def open_restaurant(self):
        #method to show if the restaurant is open or not
        print(f"{self.restro_name} is now open for dining and takeaways")
    
    def number_servings(self):
        #function to read num of servings
        print(f"We have served {self.number_served} customers today\n")


    def set_number_served(self, served):
        #function to set the number of customers served
        self.number_served = served

    def increment_servings(self, increment_no):
        #method to increment servings if it is higher then earlier
        if increment_no > self.number_served:
            self.number_served += increment_no
        else:
            print(f"We can't change the number of servings to less")


restro = Restaurant("Hope", "chinese")
restro.describe_restro()
restro.set_number_served(25)
restro.increment_servings(53)
restro.number_servings()

