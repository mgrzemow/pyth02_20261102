"""Atrybuty klasy i instancji, __slots__ oraz pierwsza prosta klasa."""
class MyClass:
    """Klasa z atrybutem klasy i atrybutami instancji w __slots__."""
    __slots__ = [
        'i_atr',
        'i_atr1',
        'i_atr2',
        'i_atr3',
    ]

    def __init__(self):
        """Ustawia atrybut instancji."""
        self.i_atr3 = 12

    # class atribute
    atr = 0
    def m1(self, v):
        """Ustawia kolejny atrybut instancji."""
        # instance atrubute - always on self
        self.i_atr = v





class Czlowiek:
    """Prosta klasa z imieniem i nazwiskiem."""
    __slots__ = [
        'imie',
        'nazwisko',
    ]
    def __init__(self, imie, nazwisko):
        """Zapamiętuje imię i nazwisko."""
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        """Wypisuje powitanie."""
        print(f'Cześć, jestem {self.imie} {self.nazwisko}.')


if __name__ == "__main__":
    a = MyClass()
    b = MyClass()
    a.m1(12)
    print(a.atr, b.atr)
    MyClass.atr = 1
    print(a.atr, b.atr)
    print(a.atr, b.atr, MyClass.atr)
    # this is ok
    a.__class__.atr = 'new val'
    print(a.atr, b.atr, MyClass.atr)
    print(a.atr, b.atr, MyClass.atr)
    # problemI assign class atribute on an instance
    # a.asdasdasd =  123123
    # a.atr = 'ooops'
    print(a.atr, b.atr, MyClass.atr)
    c = Czlowiek('Ala', 'Nowak')
