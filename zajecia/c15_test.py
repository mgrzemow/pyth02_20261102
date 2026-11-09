"""Fikstury pytest: zakres session, yield (przygotowanie i sprzątanie), parametrize."""

import pytest
from c15 import podziel

dane_testowe = [
    [(4, 2), 2],
    [(10, 5), 2],
    [(100, 5), 20],
    [(100, 50), 2],
    [(4, 2), 2],
    [(10, 5), 2],
    [(100, 5), 20],
    [(100, 50), 2],
]

dane_testowe_2 = [
    [4, 2, 2],
    [10, 5, 2],
]


@pytest.fixture(scope="session")
def udawany_fixture():
    """Fikstura bez wartości: pokazuje tylko moment startu i końca."""
    print("\n start udawany_fixture\n")
    yield
    print("\n koniec udawany_fixture\n")


# uwaga: znacznik (mark) na fiksturze w pytest 9 to błąd - znaczniki dajemy na testy
@pytest.fixture(scope="session")
def dane_testowe_fixture():
    """Udostępnia dane testowe raz na całą sesję testów."""
    print("\n start dane_testowe_fixture\n")
    yield dane_testowe
    print("\nkoniec dane_testowe_fixture\n")


# @pytest.mark.parametrize("wejscie, wyjscie", dane_testowe)
# def test_podziel_1(wejscie, wyjscie):
#     assert podziel(*wejscie) == wyjscie


# @pytest.mark.parametrize("x, y, wyjscie", dane_testowe_2)
# def test_podziel_2(x, y, wyjscie):
#     assert podziel(x, y) == wyjscie


def test_podziel_3(dane_testowe_fixture, udawany_fixture):
    """Sprawdza dzielenie na danych z fikstury, korzystając z dwóch fikstur."""
    for wejscie, wyjscie in dane_testowe_fixture:
        assert podziel(*wejscie) == wyjscie


def test_podziel_4(dane_testowe_fixture):
    """Ta sama fikstura sesyjna drugi raz: nie jest tworzona ponownie."""
    for wejscie, wyjscie in dane_testowe_fixture:
        assert podziel(*wejscie) == wyjscie
