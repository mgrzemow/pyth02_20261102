"""Narzędzia pomocnicze: pomiar czasu i logowanie wywołań funkcji."""

import functools
import logging
import time
from collections.abc import Callable
from types import TracebackType
from typing import Self

logger = logging.getLogger(__name__)


class Stoper:
    """Menedżer kontekstu mierzący czas wykonania bloku with.

    Attributes:
        opis: Opis pomiaru.
        czas: Zmierzony czas w sekundach, dostępny po wyjściu z bloku.
    """

    def __init__(self, opis: str) -> None:
        """Zapamiętuje opis pomiaru.

        Args:
            opis: Tekst wypisywany razem z wynikiem.
        """
        self.opis = opis
        self.czas = 0.0
        self._start = 0.0

    def __enter__(self) -> Self:
        """Zapisuje czas startu i zwraca stoper."""
        self._start = time.perf_counter()
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        """Zapisuje zmierzony czas; ewentualny wyjątek z bloku leci dalej."""
        self.czas = time.perf_counter() - self._start

    def __repr__(self) -> str:
        """Zwraca opis pomiaru z czasem w sekundach."""
        return f"{self.opis}: {self.czas:0.2f} s"


def loguj_wywolania[**P, R](
    poziom_ok: int = logging.DEBUG, poziom_bledu: int = logging.ERROR
) -> Callable[[Callable[P, R]], Callable[P, R]]:
    """Tworzy dekorator logujący wywołania funkcji, jej wyniki i wyjątki.

    Args:
        poziom_ok: Poziom logowania dla wywołań zakończonych sukcesem.
        poziom_bledu: Poziom logowania dla wyjątków.

    Returns:
        Dekorator zachowujący sygnaturę dekorowanej funkcji.
    """

    def dekorator(funkcja: Callable[P, R]) -> Callable[P, R]:
        """Opakowuje funkcję kodem logującym."""

        @functools.wraps(funkcja)
        def opakowana(*args: P.args, **kwargs: P.kwargs) -> R:
            """Loguje wywołanie i wynik, a wyjątek loguje i zgłasza dalej."""
            nazwa = funkcja.__name__
            logger.log(poziom_ok, "wywołanie %s, args=%r, kwargs=%r", nazwa, args, kwargs)
            try:
                wynik = funkcja(*args, **kwargs)
            except Exception as blad:
                logger.log(poziom_bledu, "%s zgłosiła %r", nazwa, blad)
                raise
            logger.log(poziom_ok, "%s zwróciła %r", nazwa, wynik)
            return wynik

        return opakowana

    return dekorator
