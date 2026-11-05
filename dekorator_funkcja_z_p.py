"""Dekorator jako funkcja, z parametrami."""

import functools


def dekorator(p1=None):
    """Przyjmuje parametr i zwraca właściwy dekorator."""

    def dekorator_wlasciwy(f_dekorowana):
        """Właściwy dekorator, opakowujący funkcję."""

        @functools.wraps(f_dekorowana)
        def nowa_funkcja(*args, **kwargs):
            """Wywołuje oryginalną funkcję i wypisuje jej wynik."""
            print("nowa_funkcja przed wywolaniem oryginalnej", args, kwargs, p1)
            r = f_dekorowana(*args, **kwargs)
            print("nowa_funkcja po wywolaniu oryginalnej", args, kwargs, r)
            return r

        return nowa_funkcja

    return dekorator_wlasciwy


@dekorator(p1=12)
def f(x):
    """Przykładowa funkcja do udekorowania."""
    print("f", x)
    return 55


if __name__ == "__main__":
    print(f(1))
