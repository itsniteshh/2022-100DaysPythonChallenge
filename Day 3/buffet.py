#starting with tupes

foods = ("chinese", "indian", "south idndian", "french style", "north indian", "punjabi")

#for food in foods:
print(foods)

foods = list(foods)

foods.pop()
foods.pop()

foods.append("italian")
foods.append("rajasthani")

foods = tuple(foods)
print(foods)