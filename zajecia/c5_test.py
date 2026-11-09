"""Testy klasy Spychacz z c5.py; uruchomienie: uv run pytest zajecia/c5_test.py."""

import pytest
from c5 import Spychacz


def test_object_creation():
    """Nowy spychacz stoi w (0, 0)."""
    s = Spychacz("kr12345")
    assert s is not None
    assert s.nr_rej == "kr12345"
    assert s._x == 0
    assert s._y == 0
    assert "0" in str(s)


def test_object_creation_raises_exception():
    """Numer rejestracyjny inny niż str daje TypeError."""
    with pytest.raises(TypeError, match="nr_rej must be a string"):
        Spychacz(123)


def test_initial_direction_n():
    """Na starcie spychacz jedzie na północ."""
    s = Spychacz("kr12345")
    s.jedz(10)
    assert s._y == 10
    assert s._x == 0


def test_go_forward():
    """Jazda z trzema skrętami w prawo."""
    s = Spychacz("kr12345")
    s.jedz(10)
    s.skrec_w_prawo()
    s.jedz(20)
    s.skrec_w_prawo()
    s.jedz(30)
    s.skrec_w_prawo()
    s.jedz(40)
    assert s._x == -20
    assert s._y == -20


def test_skrec_w_prawo():
    """Po skręcie w prawo spychacz jedzie na wschód."""
    s = Spychacz("kr12345")
    s.skrec_w_prawo()
    s.jedz(12)
    assert s._x == 12
    assert s._y == 0


def test_reset():
    """reset() wraca do pozycji i kierunku startowego."""
    s = Spychacz("kr12345")
    s.jedz(10)
    s.skrec_w_prawo()
    s.jedz(15)
    assert s._x == 15
    assert s._y == 10
    s.reset()
    assert s._x == 0
    assert s._y == 0
    assert s._kierunek == 0


def test_approx_example():
    """Porównanie liczb zmiennoprzecinkowych przez pytest.approx."""
    x = 0.1 + 0.2
    y = 0.3
    assert x == pytest.approx(y)
