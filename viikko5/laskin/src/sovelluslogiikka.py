class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self._historia = [0]
    def miinus(self, operandi):
        self._arvo = self._arvo - operandi

    def plus(self, operandi):
        self._arvo = self._arvo + operandi

    def nollaa(self):
        self._arvo = 0

    def aseta_arvo(self, arvo):
        self._arvo = arvo

    def arvo(self):
        return self._arvo
    
    def historia(self,arvo):
        self._historia.append(arvo)
    
    def kumoa(self):
        if len(self._historia) >= 2:
            self._arvo = self._historia.pop(-2)
        else:
            self._arvo = 0
    def nollaa_historia(self):
        self._historia = [0]

