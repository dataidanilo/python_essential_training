
#=================================
#          DICTIONARIES
#=================================
# sets are used to store items in key:value pairs

song = {
    "song" : "Glory Days",
    "artist" : "Bruce Springsteen",
    "year" : 1985,
    "producers" : ["Jon Landau", "Chuck Plotkin", "Bruce Springsteen", "Steven Van Zandt"] # items can be of any data type
}
print(song)
print(song["artist"])
print(len(song))
print(type(song))

song2 = dict(song = "Song 2", artist = "Blur", year = 1997) # dict() method

# access items
artist = song["artist"]
artist = song.get("artist")
print(artist)

x = song.keys()
print(x)
song["album"] = "Born in the U.S.A."
print(x)
x = song.values()
print(x)
y = song.items() # it returns all items as tuples in a list
print(y)

if "artist" in song:
    print("Yes, artist is one of the keys")

# update and add
song2["song"] = "SONG 2"
song2["rating"] = 8
song2.update({"genre":"rock"})
print(song2)

# remove
song2.pop("rating")
song2.popitem() # remove last inserted item
del song2["rating"]
song2.clear()
del song2 # to delete song2 completely

# copy dictionary
songCopy = song.copy()
songCopy = dict(song)
print(songCopy)

# nested dictionary

playlist = {
    "song1" : {
        "artist" : "The Strokes",
        "song" : "Someday"
    },
    "song2" : {
        "artist" : "The Hives",
        "song" : "Hate To Say I Told You So"
    },
    "song3" : {
        "artist" : "The Beatles",
        "song" : "Something"
    }
}

print(playlist["song1"]["artist"])

for x, obj in playlist.items():
    print(x)

    for y in obj:
        print(y + ':', obj[y])

