from SongPool import SongPool
from Song import Song

song = Song('Eminem','Rap','Stan')
song2 = Song('Kurt Cobain', 'Rock', 'The man who sold the world')
song3 = Song('Bad bunny', 'Trap', 'La cancion')
song4 = Song('Sia', 'Pop', 'Chandelier')
songs = [song, song2, song3, song4, song2]

pool = SongPool.getInstance()
pool.set_limit(5)
pool.add_songs(songs)



s = pool.acquire()
print(s.play())
pool.release(s)