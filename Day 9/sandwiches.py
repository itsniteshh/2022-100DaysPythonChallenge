

def making_sandwiches(*args):
    print(type(args))
    print(f"The following sandwiches are being ordered: ")
    for ar in args:
        print(ar)

making_sandwiches("cheeese", "mayo", "panner", "chicken")
