"""Dziedziczenie, klasy abstrakcyjne i super() na przykładzie zespołu pracowników."""
import abc
import faker


class PracownikAbstract(metaclass=abc.ABCMeta):
    """Abstrakcyjny pracownik z wypłatą zarobków."""
    __slots__ = ('imie', '_zarobki')
    def __init__(self, *, imie):
        """Ustawia imię i zeruje zarobki."""
        self.imie = imie
        self._zarobki = 0

    def wyplata(self):
        """Zwraca zarobki i zeruje licznik."""
        z = self._zarobki
        self._zarobki = 0
        return z

    @abc.abstractmethod
    def pracuj(self, ile):
        """Dolicza zarobki za podaną liczbę godzin."""
        ...

class Pracownik(PracownikAbstract):
    """Pracownik ze stawką podstawową i za nadgodziny."""
    __slots__ = ('stawka_pod', 'stawka_nad')
    def __init__(self, *,  stawka_pod, stawka_nad, **kwargs):
        """Zapamiętuje stawki."""
        super().__init__(**kwargs)
        self.stawka_pod = stawka_pod
        self.stawka_nad = stawka_nad
        self._zarobki = 0

    def pracuj(self, ile):
        """Dolicza stawkę podstawową do 8 godzin, a powyżej stawkę za nadgodziny."""
        if ile > 8:
            self._zarobki += self.stawka_nad * (ile - 8) + self.stawka_pod * 8
        else:
            self._zarobki += self.stawka_pod * ile



# Kierownik

class Kierownik(Pracownik):
    """Pracownik z premią za długi dzień."""
    __slots__ = ('bonus_kier',)
    def __init__(self, *, bonus_kier, **kwargs):
        """Zapamiętuje premię kierownika."""
        super().__init__(**kwargs)
        self.bonus_kier = bonus_kier

    def pracuj(self, ile):
        """Dolicza premię, gdy praca trwała co najmniej 10 godzin."""
        super().pracuj(ile)
        if ile >= 10:
            self._zarobki += self.bonus_kier


# Dyrektor earns bonus_dyr for each call of pracuj()

class Dyrektor(Kierownik):
    """Kierownik z premią za każde wywołanie pracuj()."""
    __slots__ = ('bonus_dyr',)
    def __init__(self, *, bonus_dyr, **kwargs):
        """Zapamiętuje premię dyrektora."""
        super().__init__(**kwargs)
        self.bonus_dyr = bonus_dyr

    def pracuj(self, ile):
        """Dolicza premię dyrektora."""
        super().pracuj(ile)
        self._zarobki += self.bonus_dyr

def zatrudnij_zespol(ilu_p, ilu_k, ilu_d) -> list[PracownikAbstract]:
    """Tworzy zespół o podanej liczbie osób na każdym stanowisku."""
    zespol = []
    f = faker.Faker('PL_pl')
    for i in range(ilu_p):
        zespol.append(Pracownik(imie=f.first_name(), stawka_pod=10, stawka_nad=20))
    for i in range(ilu_k):
        zespol.append(Kierownik(imie=f.first_name(), stawka_pod=10, stawka_nad=20, bonus_kier=100))
    for i in range(ilu_d):
        zespol.append(Dyrektor(imie=f.first_name(), stawka_pod=10, stawka_nad=20, bonus_kier=100, bonus_dyr=1000))
    return zespol


if __name__ == "__main__":
    z = zatrudnij_zespol(10, 3, 2)
    for p in z:
        p.pracuj(10)
        p.pracuj(3)
        p.pracuj(13)

    print(sum(p.wyplata() for p in z))
