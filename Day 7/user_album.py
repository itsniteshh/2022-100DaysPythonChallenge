def make_album(artist_name, album_title):
    #printing a dictionary taking two values

    album_details = {
        "artiset name": artist_name,
        "album title": album_title
        }
    return album_details

while True:
    print()
    artist_name = input("enter artist name: ")
    album_title = input("enter artist's album. press 'q' anytime to quit\n")

    if artist_name == "q" or album_title == "q":
        break

album = make_album(artist_name, album_title)
print(album)