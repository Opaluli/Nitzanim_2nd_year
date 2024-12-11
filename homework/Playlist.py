liked_songs = {
    "Shake It Off": {
        "artist": "Taylor Swift",
        "duration": (3, 23),
        "genre": "Pop"
    },
    "Shemesh": {
        "artist": "Mergi",
        "duration": (2, 33),
        "genre": "Israeli"
    },
    "Chop Suey!": {
        "artist": "System of a Down",
        "duration": (3, 30),
        "genre": "Metal"
    },
    "Mimaamakim": {
        "artist": "Idan Raichel",
        "duration": (4, 33),
        "genre": "Israeli"
    },
    "Do I Wanna Know?": {
        "artist": "Arctic Monkeys",
        "duration": (4, 26),
        "genre": "Rock"
    },
    "Love Story": {
        "artist": "Taylor Swift",
        "duration": (3, 55),
        "genre": "Pop"
    },
    "Bo’ee": {
        "artist": "Idan Raichel",
        "duration": (4, 45),
        "genre": "Israeli"
    }
}

def menu(liked_songs):
    while True:
        print(
            "WELCOME TO NITZAMUSIC!!! \n" +
             "1. ADD SONG \n" +
             "2. CHECK SONG STATUS \n" +
             "3. REMOVE ALL SONGS OFF AN ARTIST"

        )
        option = input("ENTER A NUMBER - \n")
        if option == "1":
            while True:
                song_name = input("ENTER THE SONG NAME - ")
                if song_name in liked_songs:
                    print("THE SONG ALREADY EXISTS.")
                    continue
                liked_songs.update({song_name : add_song()})
                break
            print(liked_songs)

        elif option == "2":
            song_name = input("ENTER THE SONG NAME - ")
            if song_name in liked_songs:
                answer = input(f"DO YOU WANT TO REMOVE {song_name} OF YOUR LIKED SONGS? Y/N - ")
                if answer == "Y":
                    del liked_songs[song_name]
            else:
                print("THIS SONG DOES NOT EXIST IN THE PLAYLIST. \n")
                continue

        elif option == "3":
            artist = input("ENTER ARTIST NAME - ")
            removed = False
            for song in liked_songs:
                if song



def add_song():
    artist = input("ENTER ARTIST NAME - ")
    minutes_duration = int(input("ENTER SONG LENGTH MINUTES - "))
    seconds_duration = int(input("ENTER SONG LENGTH SECONDS - "))
    genre = input("ENTER SONG GENRE - ")

    return \
        {
            "artist": artist,
            "duration": (minutes_duration, seconds_duration),
            "genre": genre
        }


def main(liked_songs):
    menu(liked_songs)


main(liked_songs)