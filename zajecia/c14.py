# mając dany koszyk walut:
koszyk =  {
    'usd': 1234,
    'chf': 1234,
    'eur': 1234,
    'czk': 1234,
    'cad': 1234,
}
# https://api.nbp.pl/api/exchangerates/rates/a/chf/?format=json
import requests
r = requests.get
r.json()

#  wycenic ten koszyk walut w oparciu o kurs walutowy
# wziety z api nbp
# uzyc concurrent.futures.ThreadPoolExecutor
