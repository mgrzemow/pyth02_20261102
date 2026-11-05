"""Ćwiczenie: dekorator zamieniający ValueError na None, także dla funkcji wbudowanej."""
# napisać dekorator, który zamienia ValueError z dekorowanej funkcji na None
import functools


def value_error_to_none(f_dekorowana):
    """Dekorator zamieniający ValueError z funkcji na None."""
    @functools.wraps(f_dekorowana)
    def nowa_funkcja(*args, **kwargs):
        """Wywołuje funkcję i przy ValueError zwraca None."""
        # przed
        try:
            return f_dekorowana(*args, **kwargs)
        except ValueError:
            return None
    return nowa_funkcja

# można ale obstawiam że to brzydko wybuchnie
int = value_error_to_none(int)

if __name__ == '__main__':
    print(int('aka'))
    x = 12
    y = 44
    print(x + y)