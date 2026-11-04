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
    _kierunki = 'NESW'
    __slots__ = ['nr_rej',
                 '_x',
                 '_y',
                 '_kierunek']

    def __init__(self, nr_rej):
        self.nr_rej = nr_rej
        self._x = 0
        self._y = 0
        self._kierunek = 0

    def skrec_w_prawo(self):
        self._kierunek = (self._kierunek + 1) % 4

    def jedz(self, dlugosc):
        if self.__class__._kierunki[self._kierunek] == 'N':
            self._y += dlugosc
        elif self.__class__._kierunki[self._kierunek] == 'E':
            self._x += dlugosc
        elif self.__class__._kierunki[self._kierunek] == 'S':
            self._y -= dlugosc
        elif self.__class__._kierunki[self._kierunek] == 'W':
            self._x -= dlugosc

    def __str__(self):
        return f'Spychacz {self.nr_rej} in ({self._x}, {self._y})'

    # if I only want one str conversion - use repr
    def __repr__(self):
        return f'Spychacz({self.nr_rej})'

    # conversions
    def __int__(self):
        return 555

    # do not do that!!!
    # danger of checking if instance
    def __bool__(self):
        return False

    def __float__(self):
        return 55.5

    # operatory

    def __add__(self, other: 'int|Spychacz'):
        return 'nie wiem co zwrocic'

    # and much more!!!

    # hashing - I MUST implement both!!!
    def __hash__(self):
        # how to calculate hash of a number of atributes
        return hash((self.nr_rej, self._x, self._y))

    def __eq__(self, other):
        return self.nr_rej == other.nr_rej

    # needed for sorting
    def __lt__(self, other):
        return self.nr_rej < other.nr_rej

    # slicing
    def __getitem__(self, item):
        print('__getitem__', item)
        return 12

    def __del__(self):
        print(
            'destructor called for Spychacz, not guarantteed to be called'
        )


if __name__ == '__main__':
    # spychzcz is born in (0,0) facing up
    s = Spychacz('kr12345')

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
        print('not None')
    else:
        print('None')

    s1 = Spychacz('wa12345')
    s + s1

    zbior = set()
    zbior.add(s)
    print(zbior)
    s2 = Spychacz('kr12345')
    zbior.add(s2)
    print(zbior)
    s.nr_rej = 'nowy'
    zbior.add(s)
    print(zbior)
    ls = [s1, s]
    ls.sort()
    print(ls)
    s[1]
    s['asdasd']
    s['asdasd':1.4:6]

















    s + s1

