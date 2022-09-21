import json
import requests

class P2PParce():
    def __init__(self) -> None:
        self.url = 'https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search'
        self.data = {
          "asset": "USDT",
          "fiat": "RUB",
        #   "merchantCheck": False,
          "page": 1,
          "payTypes": ['TinkoffNew'],
          "publisherType": None,
          "rows": 1,
          "tradeType": "BUY",
          "transAmount": 10000
        }

        self.headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Length": "123",
            "content-type": "application/json",
            "Host": "p2p.binance.com",
            "Origin": "https://p2p.binance.com",
            "Pragma": "no-cache",
            "TE": "Trailers",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0"
        }

    def getTimeLastUpdate(self):
        pass

    def getPrice(self, fiat, payType, asset, trade_type, transAmount):
        self.setup_data_headers(fiat, payType, asset, trade_type, transAmount)
        request = requests.post(self.url, headers=self.headers, json=self.data)
        self.data_list = json.loads(request.text)
        if P2PParce.check_correct_data(self.data_list):
            return P2PParce.price_for_list(self.data_list)
        else:
            return -1

    def setup_data_headers(self, fiat, payType, asset, trade_type, transAmount):
        self.data['fiat'] = fiat
        self.data['payTypes'] = [payType]
        self.data['asset'] = asset
        self.data['tradeType'] = trade_type
        self.data['transAmount'] = transAmount

    def check_correct_data(data):
        if 'data' in data:
            if data['data'] is not None:
                if len(data['data']) > 0:
                    if 'adv' in data['data'][0]:
                        if 'price' in data['data'][0]['adv']:
                            return True
        return False

    def price_for_list(data):
        return float(data['data'][0]['adv']['price'])

if __name__ == "__main__":
    p2p = P2PParce()
    for i in range(1):
        price = p2p.getPrice('RUB', 'TinkoffNew', 'USDT', 'BUY', 10000)
        print(price)
        # sleep(0.1)