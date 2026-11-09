"""Testy generatora generuj_spread z c4.py; uruchomienie: uv run pytest zajecia/c4_test.py."""

import pytest
from c4 import generuj_spread

wej = [
    {"bid": 3.89, "ask": 4.97},
    {"bid": 4.41, "ask": 5.26},
    {"bid": 4.09, "ask": 5.04},
    {"bid": 3.52, "ask": 5.18},
    {"bid": 4.29, "ask": 5.31},
    {"bid": 4.18, "ask": 5.29},
    {"bid": 4.02, "ask": 5.35},
    {"bid": 3.69, "ask": 4.8},
    {"bid": 4.37, "ask": 4.94},
    {"bid": 3.79, "ask": 4.64},
    {"bid": 3.86, "ask": 5.24},
    {"bid": 4.33, "ask": 4.64},
]
wyj = [
    {"bid": 3.89, "ask": 4.97, "spread": 1.08},
    {"bid": 4.41, "ask": 5.26, "spread": 0.85},
    {"bid": 4.09, "ask": 5.04, "spread": 0.95},
    {"bid": 3.52, "ask": 5.18, "spread": 1.66},
    {"bid": 4.29, "ask": 5.31, "spread": 1.02},
    {"bid": 4.18, "ask": 5.29, "spread": 1.11},
    {"bid": 4.02, "ask": 5.35, "spread": 1.33},
    {"bid": 3.69, "ask": 4.8, "spread": 1.11},
    {"bid": 4.37, "ask": 4.94, "spread": 0.57},
    {"bid": 3.79, "ask": 4.64, "spread": 0.85},
    {"bid": 3.86, "ask": 5.24, "spread": 1.38},
    {"bid": 4.33, "ask": 4.64, "spread": 0.31},
]
dane_testowe = list(zip(wej, wyj))


@pytest.mark.parametrize("wejscie, wyjscie", dane_testowe)
def test_generuj_spread(wejscie, wyjscie):
    """Sprawdza, że generator dokłada spread do każdego notowania."""
    assert list(generuj_spread([wejscie])) == [wyjscie]
