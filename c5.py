"""Ćwiczenie: klasa Spychacz oraz metody specjalne: konwersje, operatory, hash, sortowanie."""
# Napisz klasę Spychacz
# Spychacz pamięta:
# - nr_rej
# - x
# - y
# - kierunek
# Spcyacz umie:
# - jedz
# - skrec_w_prawo
# - wypisz_sie

#
#             |
#             |
#             |
#             |
#             |
# ------------------------
#             |
#             |
#             |
#             |
#             |


class Spychacz:
    """Pojazd poruszający się po siatce, pokazujący metody specjalne."""

    _kierunki = "NESW"
    __slots__ = ["nr_rej", "_x", "_y", "_kierunek"]

    def __init__(self, nr_rej):
        """Tworzy spychacz w punkcie (0, 0), skierowany na północ."""
        self.nr_rej = nr_rej
        self._x = 0
        self._y = 0
        self._kierunek = 0

    def skrec_w_prawo(self):
        """Obraca spychacz o 90 stopni w prawo."""
        self._kierunek = (self._kierunek + 1) % 4

    def jedz(self, dlugosc):
        """Przesuwa spychacz o podaną długość w bieżącym kierunku."""
        if self.__class__._kierunki[self._kierunek] == "N":
            self._y += dlugosc
        elif self.__class__._kierunki[self._kierunek] == "E":
            self._x += dlugosc
        elif self.__class__._kierunki[self._kierunek] == "S":
            self._y -= dlugosc
        elif self.__class__._kierunki[self._kierunek] == "W":
            self._x -= dlugosc

    def __str__(self):
        """Zwraca opis dla użytkownika: numer i pozycję."""
        return f"Spychacz {self.nr_rej} in ({self._x}, {self._y})"

    # if I only want one str conversion - use repr
    def __repr__(self):
        """Zwraca opis dla programisty."""
        return f"Spychacz({self.nr_rej})"

    # conversions
    def __int__(self):
        """Pokazuje konwersję int(); wartość jest przykładowa."""
        return 555

    # do not do that!!!
    # danger of checking if instance
    def __bool__(self):
        """Pokazuje konwersję bool(); zawsze False, co jest celowym złym przykładem."""
        return False

    def __float__(self):
        """Pokazuje konwersję float(); wartość jest przykładowa."""
        return 55.5

    # operatory

    def __add__(self, other: "int|Spychacz"):
        """Pokazuje przeciążenie operatora +."""
        return "nie wiem co zwrocic"

    # and much more!!!

    # hashing - I MUST implement both!!!
    # UWAGA: hash używa też x i y, a __eq__ tylko nr_rej, więc dwa równe obiekty
    # mogą mieć różne hashe; poprawna wersja używa w obu tych samych pól
    def __hash__(self):
        """Zwraca hash z numeru i pozycji."""
        # how to calculate hash of a number of atributes
        return hash((self.nr_rej, self._x, self._y))

    def __eq__(self, other):
        """Porównuje spychacze po numerze rejestracyjnym."""
        return self.nr_rej == other.nr_rej

    # needed for sorting
    def __lt__(self, other):
        """Porządkuje spychacze po numerze; wymagane przy sortowaniu."""
        return self.nr_rej < other.nr_rej

    # slicing
    def __getitem__(self, item):
        """Pokazuje, co trafia do operatora [], także przy wycinku."""
        print("__getitem__", item)
        return 12

    def __del__(self):
        """Destruktor; Python nie gwarantuje jego wywołania."""
        print("destructor called for Spychacz, not guarantteed to be called")


if __name__ == "__main__":
    # spychzcz is born in (0,0) facing up
    s = Spychacz("kr12345")

    print(s)  # Spychacz kr12345 in (0, 0)
    s.jedz(10)
    # 90 deg right turn
    s.skrec_w_prawo()
    print(s)  # Spychacz kr12345 in (0, 10)

    s.jedz(10)
    # 90 deg right turn
    s.skrec_w_prawo()
    print(s)  # Spychacz kr12345 in (10, 10)
    s.jedz(10)
    # 90 deg right turn
    s.skrec_w_prawo()
    print(s)  # Spychacz kr12345 in (10, 0)
    s.jedz(10)
    # 90 deg right turn
    s.skrec_w_prawo()
    print(s)  # Spychacz kr12345 in (0, 0)
    print([s])
    print(Spychacz.__slots__)
    print(s._kierunek)
    print(int(s))

    # simple mistake - should have is not None
    if s:
        print("not None")
    else:
        print("None")

    s1 = Spychacz("wa12345")
    s + s1

    zbior = set()
    zbior.add(s)
    print(zbior)
    s2 = Spychacz("kr12345")
    zbior.add(s2)
    print(zbior)
    s.nr_rej = "nowy"
    zbior.add(s)
    print(zbior)
    ls = [s1, s]
    ls.sort()
    print(ls)
    s[1]
    s["asdasd"]
    s["asdasd":1.4:6]

    s + s1
