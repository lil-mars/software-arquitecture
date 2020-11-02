from Internet import Internet
from RealInternet import RealInternet

class ProxyPattern(Internet):
    def __init__(self):
        self.internet = RealInternet()
        self.banned_sites = [ "abc.com", "def.com", "ijk.com", "lnm.com"]        

    def connect_to(self, serverhost):
        if serverhost in self.banned_sites:
            raise TypeError('El sitio esta prohibido')
        else:
            self.internet.connect_to(serverhost)