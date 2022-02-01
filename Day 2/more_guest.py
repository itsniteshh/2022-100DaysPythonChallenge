from guest_list import invite

invite.insert(3, "cristiano roanldo")
invite.append("steve jobs")

for guest in invite:
    print(f"Let's start our dinner party, {guest}")