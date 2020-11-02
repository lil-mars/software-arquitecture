from Internet import Internet

class RealInternet(Internet):
    def connect_to(self, serverhost):
        print(f'Connectando a {serverhost}')