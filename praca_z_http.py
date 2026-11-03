import requests
url_tempate = 'https://api.nbp.pl/api/exchangerates/rates/a/{}/?format=json'
currency = 'usd'
url = url_tempate.format(currency)
resp = requests.get(url)

# if resp.status_code == 200:
#     data = resp.json()
#     print(data['rates'][0]['mid'])
# else:
#     print(resp.status_code)
resp.raise_for_status()
data = resp.json()
print(data['rates'][0]['mid'])
