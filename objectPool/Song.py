class Song:
        def __init__(self, artist, genre, name):
            self.artist = artist
            self.genre = genre
            self.name = name
        
        def play(self):
            return f'La cancion: {self.name} del artista: {self.artist} y genero: {self.genre} esta Sonando !'