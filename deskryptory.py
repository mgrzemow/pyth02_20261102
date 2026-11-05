"""Property: wersja z funkcją property() i wersja z dekoratorem."""
class Czlowiek:
    """Wersja z funkcją property()."""
    __slots__ = [
        # 'imie_nazwisko',
        '_imie',
        '_nazwisko',
    ]

    def _set_imie_nazwisko(self, imie_nazwisko):
        """Rozdziela napis na imię i nazwisko."""
        self._imie, self._nazwisko = imie_nazwisko.split()

    # def _get_imie_nazwisko(self):
    #     return f'{self._imie} {self._nazwisko}'

    # imie_nazwisko = property(fget=_get_imie_nazwisko, fset=_set_imie_nazwisko)
    imie_nazwisko = property(fget=lambda self: f'{self._imie} {self._nazwisko}', fset=_set_imie_nazwisko)

    def __init__(self, imie_nazwisko):
        """Ustawia dane przez property."""
        self.imie_nazwisko = imie_nazwisko

class Czlowiek:
    """Wersja z dekoratorem @property."""
    __slots__ = [
        # 'imie_nazwisko',
        '_imie',
        '_nazwisko',
    ]

    @property
    def imie_nazwisko(self):
        """Zwraca imię i nazwisko."""
        return f'{self._imie} {self._nazwisko}'

    @imie_nazwisko.setter
    def imie_nazwisko(self, imie_nazwisko):
        """Rozdziela napis na imię i nazwisko."""
        print('setter')
        self._imie, self._nazwisko = imie_nazwisko.split()

    def __init__(self, imie_nazwisko):
        """Ustawia dane przez property."""
        self.imie_nazwisko = imie_nazwisko

    @property
    def imie_nazwisko_title(self):
        """Zwraca imię i nazwisko z wielkich liter."""
        return self.imie_nazwisko.title()

if __name__ == '__main__':
    a = Czlowiek('Ala Kowalska')
    # print(a.imie_nazwisko)
    # a.imie_nazwisko = 'ala nowak'
    # print(a.imie_nazwisko)
    # print(a.imie_nazwisko_title)
