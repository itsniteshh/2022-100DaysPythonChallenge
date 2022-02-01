sandwich_orders = ["cheese grilled", "pastrami", "pastrami", "panner cheese", "mayo grilled", "veg sandwich", "chicken sandwich", "pastrami"]

print("We have run out of pastrami")


while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

print(sandwich_orders)
