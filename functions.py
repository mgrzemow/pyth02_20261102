"""Funkcje: reguła LEGB, domknięcia i rodzaje parametrów."""
# def function_name(parameters):
#     code
#     return value


def f1(x, y):
    """Pierwsza definicja: zostanie nadpisana przez następną."""
    print("f1", x, y)


# no overloading
# second defininition overwrites the first one
def f1(x):
    """Druga definicja: to ona obowiązuje."""
    print("f1", x)


# if you really want: singledispatch, multimethod

# LEGB rule


# __name__ = 'global name'
def f2():
    """Pokazuje regułę LEGB na nazwie __name__."""

    # __name__ = 'enclosing name'
    def f2_1():
        """Wypisuje __name__ znalezione według reguły LEGB."""
        # __name__ = 'local name'
        print("f2", __name__)

    f2_1()


# f2()


# closures
def f3_pulapka():
    """Pułapka: wszystkie funkcje z pętli widzą ostatnią wartość i."""
    x = 99
    y = 33
    lista_funkcji = []
    for i in range(3):

        def f3_1():
            """Wypisuje i z domknięcia."""
            print("f3", i)

        lista_funkcji.append(f3_1)
    # domknięcie trzyma zmienną i, a nie jej wartość, więc po pętli każda funkcja widzi i == 2
    return lista_funkcji


def f3():
    """Naprawa pułapki: każda funkcja zapamiętuje własną wartość i."""
    x = 99
    y = 33
    lista_funkcji = []
    for i in range(3):

        def f3_1(i=i):
            """Wypisuje własną wartość i."""
            print("f3", i)

        lista_funkcji.append(f3_1)
    # i=i zapamiętuje bieżącą wartość i jako wartość domyślną parametru
    return lista_funkcji


# lf  = f3()
# lf[0]()
# lf[1]()
# lf[2]()


def f4(x, y, a=11, b=22):
    """Parametry pozycyjne i z wartościami domyślnymi."""
    print(f"{x=}, {y=}")
    print(f"{a=}, {b=}")


# f4(1, 2, a=3)


# zabraniam przekazywania parametrow keyword po kolejnosci
def f5(x, y, *, c=33, a=11, b=22):
    """Parametry po * można podać tylko przez nazwę."""
    print(f"{x=}, {y=}")
    print(f"{a=}, {b=}")


# f5(1, 2, 3)


def f6(x, y, *args, a=11, b=22):
    """Dodatkowe argumenty pozycyjne trafiają do *args."""
    print(f"{x=}, {y=}")
    print(f"{args=}")
    print(f"{a=}, {b=}")


# f6(1, 2, 3, 4, 5, 5, 5, 5, 4, 4, 3, 3, 3, b=999)


def f7(x, y, *args, a=11, b=22, **kwargs):
    """Dodatkowe argumenty nazwane trafiają do **kwargs."""
    print(f"{x=}, {y=}")
    print(f"{args=}")
    print(f"{a=}, {b=}")
    print(f"{kwargs=}")


# f7(1,2,3,4,5,6,7,8,9, b=99, c=999, d=888, e=666)
# f7(1,2)


def f8(*args, **kwargs):
    """Przyjmuje dowolne argumenty."""
    print(f"{args=}")
    print(f"{kwargs=}")


# f8(1,2,3,4,5,6,7,8,9, b=99, c=999, d=888, e=666)
# f8()


def f9(*args, **kwargs):
    """Przyjmuje dowolne argumenty i zwraca stałą; nadpisana przez następną definicję."""
    print(f"{args=}")
    print(f"{kwargs=}")
    return 42


def f9(slowo):
    """Zwraca ostatnią literę słowa; używana jako klucz sortowania."""
    return slowo[-1]


def print_n_times(*args, n_times=1, **kwargs):
    """Wywołuje print wielokrotnie, przekazując mu pozostałe argumenty."""
    for _ in range(n_times):
        print(*args, **kwargs)


# required keyword arguments
def f10(x, y, *, a, b):
    """Parametry a i b są wymagane i można je podać tylko przez nazwę."""
    print(f"{x=}, {y=}")
    print(f"{a=}, {b=}")


class A:
    """Klasa bazowa do przykładu z **kwargs i super()."""

    def m1(self, *, a, b):
        """Wypisuje swoje parametry."""
        print(f"A.m1 {a=}, {b=}")


class B(A):
    """Podklasa przekazująca nieznane parametry w górę."""

    def m1(self, *, c, **kwargs):
        """Odbiera c, a resztę przekazuje do klasy bazowej."""
        super().m1(**kwargs)
        print(f"B.m1 {c=}")


if __name__ == "__main__":
    lf = f3_pulapka()
    lf[0]()
    lf[1]()
    lf[2]()
    x = ["grog", "az", "zebra"]
    x.sort(key=f9)
    print(x)
    print_n_times(1, 2, 3, 4, 3, 3, 2, sep=" - ", n_times=3)
    f10(1, 2, a=3, b=4)
