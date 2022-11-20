import requests


class NBP:
    def __init__(self, body):
        self.body = body


data = NBP(body='http://api.nbp.pl/api/exchangerates/rates/a/eur/last/100/?format=json')
days = []


def currency(body):
    response = requests.get(body)
    data = response.json()

    for rate in data['rates']:
        if 4.7 > rate['mid'] > 4.5:
            continue
        else:
            days.append(f"Dzień: {rate['effectiveDate']}, Kurs: {rate['mid']}")


currency(body=data.body)

for x in days:
    print(x)