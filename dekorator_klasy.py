"""Dekorator klasy dodający atrybut i metodę."""


def dekorator(klasa):
    """Dodaje do klasy atrybut i metodę m1."""

    def m1(self, x, y):
        """Metoda dodawana do klasy; woła m2."""
        print("m1", x, y)
        self.m2()

    klasa.atr = 123
    klasa.m1 = m1
    return klasa


# @dekorator
class A:
    """Klasa rozszerzana przez dekorator."""

    def m2(self):
        """Metoda wołana przez dodaną metodę m1."""
        print("m2")

    ...


A = dekorator(A)

if __name__ == "__main__":
    print(A.atr)
    a = A()
    a.m1(1, 2)
