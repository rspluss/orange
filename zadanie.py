import requests
import json
import time
from datetime import datetime


class Exchange:
    def __init__(self, body, x=10, y=5):
        self.body = body
        self.x = x
        self.y = y


data = Exchange(body='http://api.nbp.pl/api/exchangerates/rates/a/eur/last/100/?format=json')
plik = open("log.txt", "w", encoding="utf-8")


def api(body):
    # pkt.1
    response = requests.get(body)

    # pkt.2
    pkt2 = f"{response.elapsed.total_seconds()}"

    # pkt.3
    if response.status_code != requests.codes.ok:
        pkt3 = "Coś poszło nie tak!"
    else:
        pkt3 = f"KOD odpowiedzi: {response.status_code}"

    # pkt.4
    s = requests.session()
    s.headers = headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    if response.headers['Content-Type'].split(';')[0] == 'application/json':
        pkt4 = "Format JSON"
    else:
        pkt4 = "To nie jest format JSON"

    # pkt. 5
    def jsonValidation(jsonFile):
        try:
            json.dumps(jsonFile)
        except ValueError as err:
            return False
        return True

    pkt5 = jsonValidation(response.json())

    plik.write(f"Aktualny czas: {datetime.now()} | Czas: {pkt2}, {pkt3}, {pkt4}, Walidacja: {pkt5}\n")
    return f"Aktualny czas: {datetime.now()} | Czas: {pkt2}, {pkt3}, {pkt4}, Walidacja: {pkt5}"


# pkt 6.
start_time = time.time()
while True:
    for x in range(data.x):
        print(api(body=data.body))
    time.sleep(data.y - ((time.time() - start_time) % data.y))

plik.close()
