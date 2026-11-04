class Pracownik:
    def __init__(self, *, imie, stawka_pod, stawka_nad):
        self.imie = imie
        self.stawka_pod = stawka_pod
        self.stawka_nad = stawka_nad
        self._zarobki = 0
    def pracuj(self, ile):
        if ile > 8:
            self._zarobki += self.stawka_nad * (ile - 8) + self.stawka_pod * 8
        else:
            self._zarobki += self.stawka_pod * ile
    def wyplata(self):
        z = self._zarobki
        self._zarobki = 0
        return z

# Kierownik

class Kierownik(Pracownik):
    def __init__(self, *, bonus_kier, **kwargs):
        super().__init__(**kwargs)
        self.bonus_kier = bonus_kier

    def pracuj(self, ile):
        super().pracuj(ile)
        if ile >= 10:
            self._zarobki += self.bonus_kier

# Dyrektor earns bonus_dyr for each call of pracuj()

class Dyrektor(Kierownik):
    ...

p1 = Dyrektor(imie='Jan', stawka_pod=20, stawka_nad=40, bonus_kier=100, bonus_dyr=1000)
p1.pracuj(5) # 100 + 1000
p1.pracuj(10) # 160 + 80 + 100 + 1000
print(p1.wyplata()) # 2440
print(p1.wyplata()) # 0

