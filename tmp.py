"""Szkic: dekorator funkcji i dekorator zapisany jako lambda."""

import functools


def dekorator(f_dekorowana):
    """Dekorator wypisujący informacje przed i po wywołaniu funkcji."""

    @functools.wraps(f_dekorowana)
    def nowa_funkcja(*args, **kwargs):
        """Wywołuje oryginalną funkcję i wypisuje jej wynik."""
        print("nowa_funkcja przed wywolaniem oryginalnej", args, kwargs)
        r = f_dekorowana(*args, **kwargs)
        print("nowa_funkcja po wywolaniu oryginalnej", args, kwargs, r)
        return r

    return nowa_funkcja


@dekorator
def f(x):
    """Przykładowa funkcja do udekorowania."""
    print("f", x)
    return 55


if __name__ == "__main__":
    # można zapisać jako lambda: to działa, ale jest koszmarnie nieczytelne
    dekorator_x_2 = lambda f: functools.wraps(f)(
        lambda *args, **kwargs: 2 * f(*args, **kwargs)
    )
    print(f(1))
