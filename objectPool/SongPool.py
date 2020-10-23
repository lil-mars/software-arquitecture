class SongPool:
    __instance = None
    @staticmethod 
    def getInstance():
        if SongPool.__instance == None:
            SongPool()
        return SongPool.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if SongPool.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            self.__songs = []
            self.limit = 10
            SongPool.__instance = self

    def set_limit(self, limit):
        self.limit = limit

    def add_songs(self, songs):
        if len(self.__songs) + len(songs) <= self.limit:
            self.__songs.extend(songs)
        else: 
            raise Exception('No puedes pasar el limite')

    def acquire(self):
        return self.__songs.pop()

    def release(self, song):
        self.__songs.append(song)
