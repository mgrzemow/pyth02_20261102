"""Ćwiczenie: wycena koszyka walut po kursach NBP, pobieranych równolegle przez concurrent.futures."""

import concurrent.futures as cf

import requests

# mając dany koszyk walut:
koszyk = {
    "usd": 1234,
    "chf": 1234,
    "eur": 1234,
    "czk": 1234,
    "cad": 1234,
}
# https://api.nbp.pl/api/exchangerates/rates/a/chf/?format=json
# r = requests.get
# r.json()

#  wycenic ten koszyk walut w oparciu o kurs walutowy
# wziety z api nbp
# uzyc concurrent.futures.ThreadPoolExecutor


def pobierz_kurs_waluty(waluta):
    """Pobiera średni kurs waluty z tabeli A NBP."""
    url = f"https://api.nbp.pl/api/exchangerates/rates/a/{waluta}/?format=json"
    r = requests.get(url)
    return r.json()["rates"][0]["mid"]


def wycen(k):
    """Przelicza parę (waluta, kwota) na złotówki."""
    waluta, kwota = k
    return kwota * pobierz_kurs_waluty(waluta)


if __name__ == "__main__":
    # na zajęciach użyliśmy procesów; przy samym czekaniu na sieć wystarczy ThreadPoolExecutor
    with cf.ProcessPoolExecutor(16) as executor:
        print(sum(w for w in executor.map(wycen, koszyk.items())))
