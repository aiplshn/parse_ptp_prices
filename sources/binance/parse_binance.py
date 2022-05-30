from sqlite3 import Timestamp
#from coins import coins
import requests
import json
from datetime import datetime


# TODO: Получить все курсы и распарсить
class ParseBinanceSpot():
    def __init__(self) -> None:
        self.url = 'http://www.binance.com/api/v3/ticker/price'
        self.params = '?symbol='
        self.update()

    def getPrice(self, fiat, coin):
        if fiat + coin in self.data.keys():
            return self.data[fiat+coin]
        elif coin + fiat in self.data.keys():
            return self.data[coin+fiat]
        else: 
            return -1

    def getAllPrice(self):
        return self.data

    def update(self):
        self.tikers = {}
        r = requests.get(self.url, stream=True)
        self.tikers = json.loads(r.text)
        self.toNormal()

    def toNormal(self):
        self.data = {}
        for i in self.tikers:
            self.data[i['symbol']] = i['price']

if __name__ == "__main__":
    pbs = ParseBinanceSpot()
    price = pbs.getPrice("RUB", "BTC")
    print(price)
