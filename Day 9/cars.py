def car_info(manufacturer, model_name, **car_details):
    #a dictionary that stores cars information
    print(type(car_details))
    car_details["Manufacturer"] = manufacturer
    car_details["Model name"] = model_name
    return car_details

carOrder = car_info("Tesla", "New Horizon", color ="Blue-red flame", electric = True)
print(carOrder)