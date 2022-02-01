from prettytable import PrettyTable

table = PrettyTable() #assigning instance to table var
table.align = "L" #changing default c aligh to l
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander", "Bulbasaur"]) #adding column data and their fields in lists
table.add_column("Type", ["Electrice Mouse", "Water", "Fire", "Grass"]) #repeating above
print(table)