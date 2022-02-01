class Restaurant:
    '''A class containing restaurant info like name and cuisine type'''


    def __init__(self, restro_name, cuisine_type):
        #assigning name and cuisine type attributes
        self.restro_name = restro_name
        self.cuisine_type = cuisine_type

    
    def describe_restaurant(self):
        #method for defining our restaurant
        print(f"Our restro name is {self.restro_name}" )
        print(f"We specialise in {self.cuisine_type} cuisines")

    def open_restaurant(self):
        print(f"Our restaurant is open for dining or takeaway")


restaurant1 = Restaurant("Hope", "chinese")
restaurant1.open_restaurant()
restaurant1.describe_restaurant()


