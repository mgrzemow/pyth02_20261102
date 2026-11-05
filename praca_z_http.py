"""Pobieranie kursu waluty z API NBP przez requests. Wymaga sieci."""
import requests


if __name__ == "__main__":
    url_template = 'https://api.nbp.pl/api/exchangerates/rates/a/{}/?format=json'
    currency = 'usd'
    url = url_template.format(currency)
    resp = requests.get(url)

    # if resp.status_code == 200:
    #     data = resp.json()
    #     print(data['rates'][0]['mid'])
    # else:
    #     print(resp.status_code)
    resp.raise_for_status()
    data = resp.json()
    print(data['rates'][0]['mid'])
