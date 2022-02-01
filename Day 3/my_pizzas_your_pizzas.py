from pizzas import fav_pizza

friend_pizza = fav_pizza[:]
print(friend_pizza)

fav_pizza.append("chinese pizza")
friend_pizza.append("roasted mushroom")

print(fav_pizza)
print(friend_pizza)