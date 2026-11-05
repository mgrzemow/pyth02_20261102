"""Ćwiczenie: notowania NBP jako klasa będąca jednocześnie iterowalną i iteratorem. Wymaga sieci."""

import requests
import datetime as dt
import typing

# def generatorNBP(currency: str) -> typing.Iterator[dict]:
#     url_tempate = 'https://api.nbp.pl/api/exchangerates/rates/c/{}/{}/{}/?format=json'
#     date_to = dt.date.today()
#     td1 = dt.timedelta(days=1)
#     while True:
#         date_from = date_to - 365 * td1
#         url = url_tempate.format(currency, date_from, date_to)
#         r = requests.get(url)
#         if r.status_code == 404:
#             return
#         r.raise_for_status()
#         data = r.json()
#         for rate in reversed(data['rates']):
#             del(rate['no'])
#             rate['code'] = currency
#             rate['effectiveDate'] = dt.date.fromisoformat(rate['effectiveDate'])
#             yield rate
#         date_to = date_from - td1


class NBPGenerator:
    """Iterator notowań waluty, pobierający dane latami, wstecz od dzisiaj."""

    url_template = "https://api.nbp.pl/api/exchangerates/rates/c/{}/{}/{}/?format=json"

    def __init__(self, currency: str):
        """Zapamiętuje walutę i zaczyna od bieżącej daty."""
        self.date_to = dt.date.today()
        self.currency = currency
        self._data = iter([])

    def _doczytaj_rok(self):
        """Pobiera kolejny rok notowań; po 404 nie zmienia danych."""
        td1 = dt.timedelta(days=1)
        date_from = self.date_to - 365 * td1
        url = self.__class__.url_template.format(self.currency, date_from, self.date_to)
        r = requests.get(url)
        if r.status_code == 404:
            return
        r.raise_for_status()
        self._data = reversed(r.json()["rates"])
        self.date_to = date_from - td1

    def __iter__(self):
        """Zwraca samego siebie, więc można przejść po danych tylko raz."""
        return self

    def __next__(self):
        """Zwraca następne notowanie, w razie potrzeby doczytując kolejny rok."""
        try:
            rate = next(self._data)
        except StopIteration:
            self._doczytaj_rok()
            rate = next(self._data)
        del rate["no"]
        rate["code"] = self.currency
        rate["effectiveDate"] = dt.date.fromisoformat(rate["effectiveDate"])
        return rate


# implementacja iteratora
# class BanalnyIterator:
#     def __init__(self, n):
#         self.n = n
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.n -= 1
#         if self.n > 0:
#             return self.n
#         else:
#             raise StopIteration


if __name__ == "__main__":
    for n in NBPGenerator("chf"):
        print(n)
