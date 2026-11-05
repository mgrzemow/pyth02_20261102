"""Kolejność wywołań metod metaklasy i klasy przy tworzeniu klasy i obiektu."""
# https://blog.ionelmc.ro/2015/02/09/understanding-python-metaclasses/


class Meta(type):
    """Metaklasa wypisująca kolejność swoich wywołań."""

    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        """Tworzy słownik, do którego trafi treść klasy."""
        print()
        print(f"  Meta.__prepare__({mcs=}, {name=}, {bases=}, {kwargs=})")
        return {"atr5": 99}

    # Najczęściej tu będę działać:
    def __new__(mcs, name, bases, attrs, **kwargs):
        """Tworzy obiekt klasy."""
        print()
        print(f"  Meta.__new__({mcs=}, {name=}, {bases=}, {attrs=}, {kwargs=})")
        return super().__new__(mcs, name, bases, attrs)

    def __init__(cls, name, bases, attrs, **kwargs):
        """Inicjalizuje obiekt klasy."""
        print()
        print(f"  Meta.__init__({cls=}, {name=}, {bases=}, {attrs=}, {kwargs=})")
        return super().__init__(name, bases, attrs)

    def __call__(cls, *args, **kwargs):
        """Wywoływana przy tworzeniu instancji klasy."""
        print()
        print(f"  Meta.__call__({cls=}, {args=}, {kwargs=})")
        return super().__call__(*args, **kwargs)


class A(metaclass=Meta, suffix="_get", akuku=99):
    """Klasa używająca metaklasy i jej parametrów."""

    cls_atr1 = 9

    def m1(self, x, y):
        """Przykładowa metoda."""
        print("m1", x, y)

    def __new__(cls, *args, **kwargs):
        """Tworzy instancję."""
        print()
        print(f"  Class.__new__({cls=}, {args=}, {kwargs=})")
        return super().__new__(cls)

    def __init__(self, *args, **kwargs):
        """Inicjalizuje instancję."""
        print()
        print(f"  Class.__init__({self=}, {args=}, {kwargs=})")


if __name__ == "__main__":
    a = A("Jan", "Nowak")
    # # print(a.atr5)
