from sqlite3 import Timestamp
#from coins import coins
import requests
import json
from datetime import datetime

class ParseBinanceSpot():
    def __init__(self) -> None:
        self.url = 'http://www.binance.com/api/v3/ticker/price'
        self.first_update = True
        self.timeout = 60

    def getPrice(self, fiat, coin):
        if fiat + coin in self.data.keys():
            return self.data[fiat+coin], 0
        elif coin + fiat in self.data.keys():
            return self.data[coin+fiat], 1
        else: 
            return -1, -1

    def getAllPrice(self):
        return self.data

    def update(self) -> bool:
        time_delta = 0
        if self.first_update:
            self.first_update = False
        else:
            self.time_now = datetime.now()
            time_delta = self.time_now - self.time_update
            if time_delta.seconds < self.timeout:
                return False

        self.tikers = {}
        r = requests.get(self.url, stream=True)
        self.tikers = json.loads(r.text)
        self.toNormal()
        self.time_update = datetime.now()
        return True

    def toNormal(self):
        self.data = {}
        for i in self.tikers:
            self.data[i['symbol']] = i['price']

if __name__ == "__main__":
    pbs = ParseBinanceSpot()
    pbs.update()
    price = pbs.getPrice("RUB", "BTC")
    print(price)
