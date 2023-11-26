class Ostoskori:
    def __init__(self):
        self._tuotteet = []
    
    def lisaa(self, tuote):
        self._tuotteet.append(tuote)
    
    def poista(self, tuote):
        for arvo in self._tuotteet:
            if arvo == tuote:
                self._tuotteet.remove(arvo)
                break

    def hinta(self):
        hinnat = map(lambda t: t.hinta, self._tuotteet)

        return sum(hinnat)
