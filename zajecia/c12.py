"""Ćwiczenie: dekorator z parametrami logujący wywołania; zapisuje log do log.txt."""

# napisać dekokator logujący wywołania dekorowanej funkcji
import functools
import logging

logging.basicConfig(level=logging.WARNING, filename="log.txt", filemode="w", encoding="utf-8")

# za pierwszym razem tworzymy obiekt loggera - one są singletonami per id
logger = logging.getLogger(__name__)
# a tu już zwracany ze slownika, więc to jest tanie - nie ma potrzeby jakoś przekazywać starannie
# referencji do loggerow
logger = logging.getLogger(__name__)
logger = logging.getLogger(__name__)

# ważne - loggery dziedziczą ustawienia na podstaie swoich nazw
# jeżeli stworzę logger o id: l1
l1 = logging.getLogger("l1")
# powiedzmy że to dodatkowo konfigurujemy ten logger
# to logger o id l1.l2 dostanie jego ustawienia
l2 = logging.getLogger("l1.l2")

# w __name__ mamy kwalifikowaną nazwę modułu, więc dla pliku m1 w pakiecie p1
# __name__ będzie miało wartość p1.m1
# więc jeżeli dodamy w __init__.py konfigurację loggera o id: p1
# to wszystkie pliki w pakiecie dostaną tę konfigurację


# l1.log(logging.DEBUG, 'test')


class loguj_wywolania:
    """Dekorator z parametrami logujący wywołania, wyniki i wyjątki."""

    def __init__(self, ok_level=logging.DEBUG, error_level=logging.ERROR):
        """Zapamiętuje poziomy logowania dla sukcesu i błędu."""
        self.ok_level = ok_level
        self.error_level = error_level

    def __call__(self, f_dekorowana):
        """Opakowuje dekorowaną funkcję."""

        @functools.wraps(f_dekorowana)
        def nowa_funkcja(*args, **kwargs):
            """Loguje wywołanie i wynik, a wyjątek loguje i zgłasza dalej."""
            lgr = logging.getLogger(__name__)
            lgr.log(
                self.ok_level,
                f"wywoluje funkcje {f_dekorowana.__name__} z parametrami {args=} i {kwargs=}",
            )
            try:
                r = f_dekorowana(*args, **kwargs)
            except BaseException as e:
                lgr.log(
                    self.error_level,
                    f"wywolanie funkcji {f_dekorowana.__name__} z parametrami {args=} i {kwargs=}, rzuciło wyjątek {e}, typu {type(e).__name__}, dodatakowe informacje {e.args}",
                )
                raise
            else:
                lgr.log(
                    self.ok_level,
                    f"funkcja {f_dekorowana.__name__} z parametrami {args=} i {kwargs=} -> {r}",
                )
            return r

        return nowa_funkcja


@loguj_wywolania()
def f1(x, y):
    """Dzieli x przez y."""
    return x / y


if __name__ == "__main__":
    f1(1, 2)
    # dekorator loguje wyjątek i zgłasza go dalej
    try:
        f1(1, 0)
    except ZeroDivisionError as e:
        print("ZeroDivisionError:", e)
