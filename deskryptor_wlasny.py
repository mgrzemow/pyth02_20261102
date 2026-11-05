"""Własny deskryptor zapamiętujący historię wartości."""
import collections
class MojDeskryptor:
    """Deskryptor zapisujący wartość w instancji i historię zmian."""
    def __init__(self, atr_name=None):
        """Zapamiętuje nazwę atrybutu i tworzy historię."""
        self.atr_name = atr_name
        self._history = collections.defaultdict(list)
    # called when a class is created
    # with this descriptor as class atribute value
    def __set_name__(self, owner, name):
        """Domyślnie nazywa atrybut od nazwy pola, z podkreśleniem."""
        if self.atr_name is None:
            self.atr_name = '_' + name

    def __set__(self, instance, value):
        """Dopisuje wartość do historii i zapisuje ją w instancji."""
        self._history[id(instance)].append(value)
        # print(self._history)
        # print('__set__', instance, value)
        setattr(instance, self.atr_name, value)

    def __get__(self, instance, owner):
        """Zwraca wartość z instancji, a przy dostępie przez klasę deskryptor."""
        print('__get__', instance, owner)
        if instance is not None:
            return getattr(instance, self.atr_name)
        else:
            return self

class Czlowiek:
    """Klasa z polami obsługiwanymi przez deskryptor."""
    __slots__ = [
        # deskryptor wiek jest atrybutem klasy, więc w __slots__ musi być inna nazwa
        '_wiek',
        '_imie_nazwisko',
    ]

    imie_nazwisko = MojDeskryptor()
    wiek = MojDeskryptor()

    def __init__(self, imie_nazwisko):
        """Ustawia imię i nazwisko przez deskryptor."""
        self.imie_nazwisko = imie_nazwisko


if __name__ == '__main__':
    a = Czlowiek('Ala Kowalska')
    print(a.imie_nazwisko)
    a.imie_nazwisko = 'ala nowak'
    a.imie_nazwisko = 'tomek nowak'
    a.imie_nazwisko = 'karol nowak'
    # print(a.imie_nazwisko)
    b = Czlowiek('asdasd')
    b.imie_nazwisko = 'adad'
    b.imie_nazwisko = 'asdasad'
    b.imie_nazwisko = 'asdfafsdfsdf'

    # print(b.imie_nazwisko._history)
    print(Czlowiek.imie_nazwisko._history)