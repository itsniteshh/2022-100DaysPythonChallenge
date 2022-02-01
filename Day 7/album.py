def make_album(artist_name, album_title):
    #printing a dictionary taking two values

    album_details = {
        "artiset name": artist_name,
        "album title": album_title
        }
    return album_details


new_album = make_album("Nitesh", "I'll be better")
print(new_album) 

new_album1 = make_album("nits", "I'll be the best")
print(new_album1) 