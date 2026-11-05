# 1. connect to
# https://api.nbp.pl/api/exchangerates/rates/a/gbp/2012-01-01/2012-01-31/?format=json
# to be able to pull a series of rates
# and present them in a for loop

"""Ćwiczenie: potok generatorów przetwarzających notowania NBP. Wymaga sieci.


Napisać generator, który będzie zwracał wszystkie dostępne notowania waluty o podanym kodzie z API NBP:

http://api.nbp.pl

Generator będzie wczytywał dane latami (wolno wysłać zapytanie tylko o rok danych na raz) i będzie zwracał (yield)notowania w kolejności odwrotnej chronologicznie (w tył).

Format pojedynczego notowania będzie słownikiem o postaci:
{"no":"21/C/NBP/2012","effectiveDate":"2012-01-31","bid":5.0382,"ask":5.1400}

{
    'code': 'USD',
        'bid': 3.3,
        'ask': 3.4,
        'effectiveDate': <tutaj obiekt date z datą notowania>
}

Proponuję skorzystać z usługi:
https://api.nbp.pl/api/exchangerates/rates/c/gbp/2012-01-01/2012-01-31/?format=json

Zwróćcie uwagę, że w URLu są zawarte: kod waluty, i obie daty.
Jak wysłać zapytanie i przeczytać odpowiedź:

r = requests.get("https://api.nbp.pl/api/exchangerates/rates/c/gbp/2012-01-01/2012-01-31/?format=json")

# Sprawdzanie statusu zapytania:
# if r.status_code != 200:
#     print('coś nie tak', r.status_code)
#     exit()

# lub:
# r.raise_for_status()

# Format JSON to po prostu zagnieżdżona struktura słowników i list, a więc np cena bid # pierwszego notowania:
j = r.json()
print(j["rates"][0]["bid"])

Możemy oczywiście po listach iterować za pomocą pętli for.

Korzystamy z pakietu requests, który trzeba ściągnąć i zainstalować.
Aby to zrobić wpisujemy w oknie Terminal w Pycharm polecenie:
pip install requests

Dodadkowo dla ambitnych napisać 3 generatory przetwarzające notowania strumieniowo:
# 1. Wyliczał spread i dodawał do notowania jako wartość dla klucza 'spread'
# 2. Wyliczał zmianę względem dnia poprzedniego (dla ceny ask) - i dodawał do notowania jako wartość dla klucza 'delta'
# 3. Generator filtrujący, który będzie puszczał dalej tylko notowania spełniające warunek:
#    wartosc bezwzględna pola o nazwie nazwa_pola >= min wartosc

Ostatecznie chciałbym mieć możliwość np znaleźć notowania USD w których spread >= 0.08 i zmiana względem dnia poprzedniego była >=0.07:

g_nbp = generatorNBP("usd")
g1 = generuj_spread(g_nbp)
g2 = generuj_delta(g1)
g3 = filtruj(g2, "spread", 0.08)
g4 = filtruj(g3, "delta", 0.07)
for n in g4:
    print(n)
"""

import requests
import datetime as dt
import typing
import itertools


def generatorNBP(currency: str) -> typing.Iterator[dict]:
    """Zwraca notowania waluty wstecz od dzisiaj, pobierając dane latami."""
    url_template = "https://api.nbp.pl/api/exchangerates/rates/c/{}/{}/{}/?format=json"
    date_to = dt.date.today()
    td1 = dt.timedelta(days=1)
    while True:
        date_from = date_to - 365 * td1
        url = url_template.format(currency, date_from, date_to)
        r = requests.get(url)
        if r.status_code == 404:
            return
        r.raise_for_status()
        data = r.json()
        for rate in reversed(data["rates"]):
            del rate["no"]
            rate["code"] = currency
            rate["effectiveDate"] = dt.date.fromisoformat(rate["effectiveDate"])
            yield rate
        date_to = date_from - td1


def generuj_spread(g_nbp) -> typing.Iterator[dict]:
    """Dodaje do notowania pole spread, czyli ask - bid."""
    for rate in g_nbp:
        rate["spread"] = round(rate["ask"] - rate["bid"], 6)
        yield rate


def generuj_delta(g_nbp) -> typing.Iterator[dict]:
    """Dodaje do notowania pole delta, czyli zmianę ceny ask względem poprzedniego dnia."""
    for rate1, rate2 in itertools.pairwise(g_nbp):
        rate1["delta"] = round(rate1["ask"] - rate2["ask"], 6)
        yield rate1


def filtruj(g_nbp, field, min):
    """Przepuszcza notowania, w których wartość bezwzględna pola wynosi co najmniej min."""
    for rate in g_nbp:
        if abs(rate[field]) >= min:
            yield rate


if __name__ == "__main__":
    g1 = generatorNBP("usd")
    g2 = generuj_spread(g1)
    g3 = generuj_delta(g2)
    g4 = filtruj(g3, "spread", 0.08)
    g5 = filtruj(g4, "delta", 0.07)

    for r in g5:
        print(r)
