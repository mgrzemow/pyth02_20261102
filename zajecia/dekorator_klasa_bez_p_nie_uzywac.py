"""Dekorator jako klasa bez parametrów: wersja niepolecana, tylko do pokazania."""

import functools

# tej wersji nie używamy - zamiast tego zwykła funkcja!!!
# da się naprawić ale po co?


class dekorator:
    """Dekorator jako klasa; bez __get__ nie zadziałałby na metodach."""

    def __init__(self, f):
        """Zapamiętuje dekorowaną funkcję."""
        self.f_dekorowana = f

    def __call__(self, *args, **kwargs):
        """Wywołuje funkcję i wypisuje jej wynik."""
        print("nowa_funkcja przed wywolaniem oryginalnej", args, kwargs)
        r = self.f_dekorowana(*args, **kwargs)
        print("nowa_funkcja po wywolaniu oryginalnej", args, kwargs, r)
        return r

    def __get__(self, instance, owner):
        """Wiąże instancję, żeby dekorator działał na metodach."""
        return functools.partial(self, instance)


class A:
    """Klasa z udekorowaną metodą."""

    @dekorator
    def m1(self, x):
        """Przykładowa metoda do udekorowania."""
        print("m1", x)
        return 55


if __name__ == "__main__":
    a = A()
    print(a.m1(1))
