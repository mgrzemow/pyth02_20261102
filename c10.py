"""Ćwiczenie: dekorator konwertujący wynik funkcji na int albo float."""
# napisać dekorator, który
# próbuje skonwertować wartość zwracaną do int
# jak się nie uda to próbuje do float
# jak się nie uda do float to się wywala z ValueError
import functools


def to_int_or_float(f_dekorowana):
    """Dekorator konwertujący wynik na int, a gdy się nie uda, na float."""
    @functools.wraps(f_dekorowana)
    def nowa_funkcja(*args, **kwargs):
        """Wywołuje funkcję i konwertuje jej wynik."""
        # przed
        r = f_dekorowana(*args, **kwargs)
        # po
        try:
            return int(r)
        except ValueError as e:
            ...

        try:
            return float(r)
        except ValueError as e:
            raise ValueError('Moj error message') from e
    return nowa_funkcja

@to_int_or_float
def f(x):
    """Zwraca argument bez zmian, żeby pokazać działanie dekoratora."""
    return x

if __name__ == '__main__':
    print(f('1'))
    print(f('1.4'))
    print(f(1.5))
    # tej wartości nie da się skonwertować, więc dekorator zgłasza ValueError
    try:
        print(f('asdasd'))
    except ValueError as e:
        print('ValueError:', e)
