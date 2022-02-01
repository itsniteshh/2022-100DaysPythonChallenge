class Restaurant:
    '''A class containing restaurant info like name and cuisine type'''


    def __init__(self, restro_name, cuisine_type):
        #assigning name and cuisine type attributes
        self.restro_name = restro_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served = 0

    
    def describe_restaurant(self):
        #method for defining our restaurant
        print(f"Our restro name is {self.restro_name}" )
        print(f"We specialise in {self.cuisine_type} cuisines")

    def open_restaurant(self):
        print(f"Our restaurant is open for dining or takeaway")

    def served(self):
        #printing the total num served
        print(f"\nThe restaurant has served {self.number_served} orders today")

    def set_num_served(self, new_no):
        #setting the servings to new no.
        self.number_served = new_no

    def increment_servings(self, inc):
        #incrementing the serving numbers
        if inc > self.number_served:
            self.number_served += inc

        else:
            print("You cannot decrease the serving value")


restaurant1 = Restaurant("Hope", "chinese")

restaurant1.open_restaurant()
restaurant1.describe_restaurant()
#setting value 
restaurant1.set_num_served(20) 

#incrementing value
restaurant1.increment_servings(42)

restaurant1.served()


