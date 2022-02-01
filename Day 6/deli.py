sandwich_orders = ["cheese grilled", "panner cheese", "mayo grilled", "veg sandwich", "chicken sandwich"]

finished_sandwich = []

while sandwich_orders:
    #removing values from list
    current_sandwich = sandwich_orders.pop()

    #printing current value to be removed
    print(f"Finishing {current_sandwich}")
    
    #appending current value to the finished list
    finished_sandwich.append(current_sandwich)

print(f"\nFollowing sandwiches are ready: ")
for sandwiches in finished_sandwich:
    print(sandwiches)


