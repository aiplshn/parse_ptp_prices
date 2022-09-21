import requests
import json

class ParseBinanceSpot():
    def __init__(self) -> None:
        self.url = 'http://www.binance.com/api/v3/ticker/price'
        self.param = {'symbol':''}

    #TODO refactor me
    def getPrice(self, fiat, coin):
        self.param['symbol'] = fiat + coin
        ticker = self.getTicker()
        if 'price' in ticker:
            return ticker['price'], 0
        else:
            self.param['symbol'] = coin + fiat
            ticker = self.getTicker()
            if 'price' in ticker:
                return ticker['price'], 1
        return -1, -1

    def getTicker(self):
        r = requests.get(self.url, stream=True, params=self.param)
        return json.loads(r.text)

    def getAllPrice(self):
        return self.data

if __name__ == "__main__":
    pbs = ParseBinanceSpot()
    for i in range(1):
        price = pbs.getPrice("RUB", "BTC")
        print(price)
