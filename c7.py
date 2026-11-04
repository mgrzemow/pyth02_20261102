import requests
import datetime as dt
import typing

def generatorNBP(currency: str) -> typing.Iterator[dict]:
    url_tempate = 'https://api.nbp.pl/api/exchangerates/rates/c/{}/{}/{}/?format=json'
    date_to = dt.date.today()
    td1 = dt.timedelta(days=1)
    while True:
        date_from = date_to - 365 * td1
        url = url_tempate.format(currency, date_from, date_to)
        r = requests.get(url)
        if r.status_code == 404:
            return
        r.raise_for_status()
        data = r.json()
        for rate in reversed(data['rates']):
            del(rate['no'])
            rate['code'] = currency
            rate['effectiveDate'] = dt.date.fromisoformat(rate['effectiveDate'])
            yield rate
        date_to = date_from - td1

# implementacja iteratora
class BanalnyIterator:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        self.n -= 1
        if self.n > 0:
            return self.n
        else:
            raise StopIteration


for i in BanalnyIterator(10):
    print(i)