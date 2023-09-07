class Song:
    count = 0
    genres=[]
    artists=[]
    genre_count={}
    artist_count={}

    def __init__(self, name, artist, genre=[]):
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)
        self.name = name
        self.artist = artist
        self.genre = genre

    @classmethod
    def add_song_to_count(cls, increment=1):
        cls.count += increment

    @classmethod
    def add_to_genres(cls, genre):
        cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
            if genre not in cls.genre_count:
                Song.genre_count[genre] = 1
            else:
                Song.genre_count[genre] += 1

    @classmethod
    def add_to_artist_count(cls, artist):
            if artist not in cls.artist_count:
                Song.artist_count[artist] = 1
            else:
                Song.artist_count[artist] += 1