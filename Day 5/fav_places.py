favourite_places = {
    "nitesh": ["everywhere"],
    "arjun": ["rajasthan", "manali", "jammu"],
    "purnima": ["assam", "himachal"]
}

for k, v in favourite_places.items():
    print(f"\n{k} wants to travel:")
    for val in v:
        print(val)