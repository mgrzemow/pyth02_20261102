"""Testy polecenia kursy-nbp, bez dostępu do sieci."""

import datetime as dt

import pytest
from typer.testing import CliRunner

from kursy_nbp import cli


def test_wypisuje_tyle_notowan_ile_limit(monkeypatch: pytest.MonkeyPatch) -> None:
    """Polecenie wypisuje najwyżej tyle linii, ile podano w --limit."""
    dane = [
        {
            "bid": 3.9,
            "ask": 4.0,
            "code": "usd",
            "effectiveDate": dt.date(2026, 1, dzien),
        }
        for dzien in range(1, 6)
    ]
    monkeypatch.setattr(cli, "pobierz_notowania", lambda waluta: iter(dane))

    wynik = CliRunner().invoke(cli.app, ["usd", "--limit", "2"])

    assert wynik.exit_code == 0
    assert len(wynik.output.splitlines()) == 2
    assert "2026-01-01 usd" in wynik.output
