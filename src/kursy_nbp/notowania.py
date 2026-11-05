"""Generatory pobierające notowania walut z API NBP i przetwarzające je strumieniowo."""

import datetime as dt
import itertools
from collections.abc import Iterable, Iterator
from typing import Any

import requests

URL = "https://api.nbp.pl/api/exchangerates/rates/c/{}/{}/{}/?format=json"
LIMIT_CZASU_S = 10

type Notowanie = dict[str, Any]


def pobierz_notowania(waluta: str) -> Iterator[Notowanie]:
    """Zwraca notowania waluty wstecz od dzisiaj, pobierając dane po jednym roku.

    Args:
        waluta: Kod waluty, np. "usd".

    Yields:
        Notowanie z polami bid, ask, code i effectiveDate jako obiektem date.

    Raises:
        requests.HTTPError: Gdy serwer zwróci błąd inny niż 404, który oznacza koniec danych.
    """
    data_do = dt.date.today()
    dzien = dt.timedelta(days=1)
    while True:
        data_od = data_do - 365 * dzien
        odpowiedz = requests.get(URL.format(waluta, data_od, data_do), timeout=LIMIT_CZASU_S)
        if odpowiedz.status_code == 404:
            return
        odpowiedz.raise_for_status()
        for notowanie in reversed(odpowiedz.json()["rates"]):
            del notowanie["no"]
            notowanie["code"] = waluta
            notowanie["effectiveDate"] = dt.date.fromisoformat(notowanie["effectiveDate"])
            yield notowanie
        data_do = data_od - dzien


def generuj_spread(notowania: Iterable[Notowanie]) -> Iterator[Notowanie]:
    """Dodaje do każdego notowania pole spread, czyli różnicę ask i bid.

    Args:
        notowania: Strumień notowań z polami ask i bid.

    Yields:
        Notowanie z dodatkowym polem spread.
    """
    for notowanie in notowania:
        notowanie["spread"] = round(notowanie["ask"] - notowanie["bid"], 6)
        yield notowanie


def generuj_delta(notowania: Iterable[Notowanie]) -> Iterator[Notowanie]:
    """Dodaje pole delta, czyli zmianę ceny ask względem notowania z poprzedniego dnia.

    Notowania płyną wstecz w czasie, więc poprzedni dzień to następny element strumienia.
    Najstarsze notowanie nie ma z czym się porównać, dlatego nie trafia do wyniku.

    Args:
        notowania: Strumień notowań w kolejności od najnowszego.

    Yields:
        Notowanie z dodatkowym polem delta.
    """
    for notowanie, poprzednie in itertools.pairwise(notowania):
        notowanie["delta"] = round(notowanie["ask"] - poprzednie["ask"], 6)
        yield notowanie


def filtruj(notowania: Iterable[Notowanie], pole: str, min_wartosc: float) -> Iterator[Notowanie]:
    """Przepuszcza notowania, w których wartość bezwzględna pola jest wystarczająco duża.

    Args:
        notowania: Strumień notowań.
        pole: Nazwa sprawdzanego pola.
        min_wartosc: Najmniejsza dopuszczalna wartość bezwzględna.

    Yields:
        Notowania spełniające warunek.
    """
    for notowanie in notowania:
        if abs(notowanie[pole]) >= min_wartosc:
            yield notowanie
