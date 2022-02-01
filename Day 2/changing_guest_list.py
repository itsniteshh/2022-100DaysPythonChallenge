from guest_list import invite

cannot_come = invite.pop()
print(f"Sorry to inform you fellas, but it looks like {cannot_come} can't make it to dinner with us")

invite.append("aliens")
for guest in invite:
    print(f"Welcome to the dinner party {guest}")