"""Polecenie kursy-nbp: wypisuje najnowsze notowania waluty."""

import itertools
from typing import Annotated

import typer

from kursy_nbp.notowania import filtruj, generuj_spread, pobierz_notowania

app = typer.Typer(add_completion=False, help="Notowania walut z API NBP.")


@app.command()
def pokaz(
    waluta: Annotated[str, typer.Argument(help="Kod waluty, np. usd.")],
    limit: Annotated[int, typer.Option(help="Ile notowań wypisać.")] = 5,
    min_spread: Annotated[float, typer.Option(help="Najmniejszy spread.")] = 0.0,
) -> None:
    """Wypisuje najnowsze notowania waluty ze spreadem nie mniejszym niż podany."""
    strumien = filtruj(generuj_spread(pobierz_notowania(waluta)), "spread", min_spread)
    for notowanie in itertools.islice(strumien, limit):
        typer.echo(
            f"{notowanie['effectiveDate']} {notowanie['code']} "
            f"bid={notowanie['bid']} ask={notowanie['ask']} spread={notowanie['spread']}"
        )
