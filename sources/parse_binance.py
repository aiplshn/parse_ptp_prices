from sqlite3 import Timestamp
from coins import coins
import requests
import json
from datetime import datetime

class ParseBinanceSpot():
    def __init__(self) -> None:
        self.url = 'http://www.binance.com/api/v3/ticker/price'
        self.params = '?symbol='

    def getPrice(self, fiat, coin):
        data = {}
        r = requests.get(self.url+self.params+fiat+coin, stream=True)
        data = json.loads(r.text)
        if data.get('code'):
            r = requests.get(self.url+self.params+coin+fiat, stream=True)
            data = json.loads(r.text)
            if data.get('code'):
                return -1
        return data

def getPrice(fiat, coin):
    data = {}
    r = requests.get("http://www.binance.com/api/v3/ticker/price?symbol="+fiat+coin, stream=True)
    data = json.loads(r.text)
    if data.get('code'):
        r = requests.get("http://www.binance.com/api/v3/ticker/price?symbol="+coin+fiat, stream=True)
        data = json.loads(r.text)
        if data.get('code'):
            return -1
    return data

def getOrders():
    
    # data = json.loads(r.text)
    
    now = datetime.now()
    timestamp = now.timestamp()
    r = requests.get(url=f"http://www.binance.com/api/v3/allOrderList?timestamb={timestamp}&symbol=BTCUSDT", headers={'X-MBX-APIKEY':'ca08kujgTbTdqnNIlIBj3bSUm1sghiaztur8BonXbXwJrog07hg1F4iMkz3lddmG'})
    print(r.text)
    print(int(timestamp))

if __name__ == "__main__":
    getOrders()