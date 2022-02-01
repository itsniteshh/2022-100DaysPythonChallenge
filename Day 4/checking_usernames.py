from types import new_class


current_users = ["itsnitesh", "iamnittzz", "admin", "noturfullmoon", "cristiano", "urstrulynitesh", "nitesh_who"]

new_users = ["alpha", "beta", "gamma", "centauri", "xyz", "iamnittzz", "admin", "noturfullmoon", "cristiano"]


for users in new_users:
    if users in current_users:
        print(f"you need to choose another username for {users}")
    else:
        print(f"yayyaya! the username {users} is available")

        