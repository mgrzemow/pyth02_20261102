"""Testy stopera i dekoratora logującego."""

import logging

import pytest

from kursy_nbp.narzedzia import Stoper, loguj_wywolania


def test_stoper_mierzy_czas() -> None:
    """Po wyjściu z bloku stoper zna czas i wypisuje go w opisie."""
    with Stoper("pomiar") as stoper:
        sum(range(1000))
    assert stoper.czas > 0
    assert repr(stoper).startswith("pomiar: ")


def test_stoper_nie_wycisza_wyjatku() -> None:
    """Wyjątek z bloku leci dalej, a czas i tak zostaje zapisany."""
    stoper = Stoper("pomiar")
    with pytest.raises(ValueError), stoper:
        raise ValueError("błąd")
    assert stoper.czas >= 0


def test_loguje_wynik(caplog: pytest.LogCaptureFixture) -> None:
    """Dekorator zachowuje wynik i loguje wywołanie."""

    @loguj_wywolania()
    def dodaj(x: int, y: int) -> int:
        """Dodaje dwie liczby."""
        return x + y

    with caplog.at_level(logging.DEBUG):
        assert dodaj(1, 2) == 3
    assert "dodaj zwróciła 3" in caplog.text


def test_loguje_wyjatek_i_zglasza_go(caplog: pytest.LogCaptureFixture) -> None:
    """Wyjątek jest logowany i zgłaszany dalej."""

    @loguj_wywolania()
    def podziel(x: int, y: int) -> float:
        """Dzieli x przez y."""
        return x / y

    with pytest.raises(ZeroDivisionError):
        podziel(1, 0)
    assert "ZeroDivisionError" in caplog.text
