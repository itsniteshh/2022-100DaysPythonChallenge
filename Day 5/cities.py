cities = {
    "mumbai": {
        "country": "India",
        "population": "30 crs",
        "fact": "city of dreams"
    },
    "pune": {
        "country": "india",
        "population": "10 crs",
        "fact": "city of workers"

    },
    "manali": {
        "country": "india",
        "population": "3 crs",
        "fact": "city of travellers"
    }
}


for k, value in cities.items():
    print(f"\nFollowing are the info about {k}:")
    for v in value.items():
        print(v)