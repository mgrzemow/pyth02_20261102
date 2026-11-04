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
    url_template = 'https://api.nbp.pl/api/exchangerates/rates/c/{}/{}/{}/?format=json'
    class NBPGeneratorIterator:
        def __init__(self, g):
            self._g = g
            self._i = 0

        def __next__(self):
            if self._i >= len(self._g._data):
                self._g._doczytaj_rok()
            rate = self._g._data[self._i].copy()
            self._i += 1
            del rate['no']
            rate['code'] = self._g.currency
            rate['effectiveDate'] = dt.date.fromisoformat(rate['effectiveDate'])
            return rate

        def __iter__(self):
            return self

    def __init__(self, currency: str):
        self.date_to = dt.date.today()
        self.currency = currency
        self._data = []

    def _doczytaj_rok(self):
        td1 = dt.timedelta(days=1)
        date_from = self.date_to - 365 * td1
        url = self.__class__.url_template.format(self.currency, date_from, self.date_to)
        print(url)
        r = requests.get(url)
        if r.status_code == 404:
            raise StopIteration()
        r.raise_for_status()
        self._data += reversed(r.json()['rates'])
        self.date_to = date_from - td1

    def __iter__(self):
        return NBPGenerator.NBPGeneratorIterator(self)


g = NBPGenerator('chf')
it1 = iter(g)
it2 = iter(g)

for i, n in zip(range(500), it1):
    ...
    #print(n)
print(1)
for i, n in zip(range(500), it2):
    ...
print(2)
for i, n in zip(range(500), it2):
    ...
