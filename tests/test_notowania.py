"""Testy generatorów notowań, bez dostępu do sieci."""

import datetime as dt
from unittest.mock import MagicMock

import pytest
import requests

from kursy_nbp import notowania as nb


@pytest.fixture
def strumien() -> list[nb.Notowanie]:
    """Zwraca notowania od najnowszego, jak w odpowiedzi przetworzonej przez generator."""
    return [
        {"bid": 3.90, "ask": 4.00},
        {"bid": 3.80, "ask": 3.95},
        {"bid": 3.70, "ask": 3.85},
    ]


def odpowiedz(status: int, stawki: list[dict[str, object]] | None = None) -> MagicMock:
    """Tworzy atrapę odpowiedzi HTTP."""
    atrapa = MagicMock(spec=requests.Response)
    atrapa.status_code = status
    atrapa.json.return_value = {"rates": stawki or []}
    return atrapa


def test_spread(strumien: list[nb.Notowanie]) -> None:
    """Spread to różnica ask i bid."""
    wynik = list(nb.generuj_spread(strumien))
    assert wynik[0]["spread"] == pytest.approx(0.10)
    assert wynik[2]["spread"] == pytest.approx(0.15)


def test_delta_pomija_najstarsze(strumien: list[nb.Notowanie]) -> None:
    """Delta porównuje z poprzednim dniem, więc najstarsze notowanie wypada."""
    wynik = list(nb.generuj_delta(strumien))
    assert len(wynik) == 2
    assert wynik[0]["delta"] == pytest.approx(0.05)


@pytest.mark.parametrize(
    ("min_wartosc", "ile"),
    [(0, 3), (0.5, 2), (2, 1), (3, 0)],
)
def test_filtruj(min_wartosc: float, ile: int) -> None:
    """Filtr bierze pod uwagę wartość bezwzględną."""
    dane: list[nb.Notowanie] = [{"x": 0.1}, {"x": -1}, {"x": 2}]
    assert len(list(nb.filtruj(dane, "x", min_wartosc))) == ile


def test_pobierz_konczy_po_404(monkeypatch: pytest.MonkeyPatch) -> None:
    """Generator odwraca kolejność, przetwarza pola i kończy pracę po 404."""
    stawki = [
        {"no": "1", "effectiveDate": "2026-01-01", "bid": 1.0, "ask": 2.0},
        {"no": "2", "effectiveDate": "2026-01-02", "bid": 1.5, "ask": 2.5},
    ]
    get = MagicMock(side_effect=[odpowiedz(200, stawki), odpowiedz(404)])
    monkeypatch.setattr(requests, "get", get)

    wynik = list(nb.pobierz_notowania("usd"))

    assert [n["effectiveDate"] for n in wynik] == [
        dt.date(2026, 1, 2),
        dt.date(2026, 1, 1),
    ]
    assert wynik[0]["code"] == "usd"
    assert "no" not in wynik[0]
    assert get.call_count == 2
    assert get.call_args.kwargs["timeout"] == nb.LIMIT_CZASU_S


def test_pobierz_zglasza_blad_serwera(monkeypatch: pytest.MonkeyPatch) -> None:
    """Błąd inny niż 404 trafia do wywołującego."""
    atrapa = odpowiedz(500)
    atrapa.raise_for_status.side_effect = requests.HTTPError("500")
    monkeypatch.setattr(requests, "get", MagicMock(return_value=atrapa))

    with pytest.raises(requests.HTTPError):
        next(nb.pobierz_notowania("usd"))
