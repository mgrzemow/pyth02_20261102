"""Dekorator jako klasa, z parametrami."""
import functools

class dekorator:
    """Dekorator z parametrami zapisany jako klasa."""
    def __init__(self, p1):
        """Zapamiętuje parametr dekoratora."""
        self.p1 = p1

    def __call__(self, f_dekorowana):
        """Opakowuje dekorowaną funkcję."""
        @functools.wraps(f_dekorowana)
        def nowa_funkcja(*args, **kwargs):
            """Wywołuje oryginalną funkcję i wypisuje jej wynik."""
            print('nowa_funkcja przed wywolaniem oryginalnej', args, kwargs, self.p1)
            r = f_dekorowana(*args, **kwargs)
            print('nowa_funkcja po wywolaniu oryginalnej', args, kwargs, r)
            return r
        return nowa_funkcja

@dekorator(p1=12)
def f(x):
    """Przykładowa funkcja do udekorowania."""
    print('f', x)
    return 55


if __name__ == "__main__":
    print(f(1))
