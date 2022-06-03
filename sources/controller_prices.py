from ast import While
from cgi import test
from parse_best_change.sources.best_change.controller_bc import BCController
from parse_best_change.sources.binance.binanceController import ControllerBinance
import threading
import time
import datetime

# Класс контролер курсов
class ControllerPrices:
    def __init__(self):
        self.best_change_controller = BCController()
        self.binance_controller = ControllerBinance()
        #self.update()
        threading.Timer(1, self.update).start()

    def newConnection(self) -> int:
        return self.best_change_controller.newConnection()

    def closeConnection(self, id: int):
        self.best_change_controller.closeConnection(id)

    def test(self):
        while True:
            time.sleep(10)
            now = datetime.datetime.now()
            print("Time out"+str(now))

    def update(self):
        while True:
            self.best_change_controller.update()
            self.binance_controller.update()
            time.sleep(960)            
            now = datetime.datetime.now()
            print("Time out "+str(now))

    #TODO add close all connection (destructor)

    def getSpotPrice(self, fiat:str, coin:str, transAmount:float):
        #return self.binance_controller.getPriceSpot(fiat, coin)
        price, side = self.binance_controller.getPriceSpot(fiat, coin)
        bank_out = 0
        coins = ''
        if side == 0:
            bank_out = transAmount * float(price)
            coins = fiat+coin
        elif side == 1:
            bank_out = transAmount / float(price)
            coins = coin+fiat
        else:
            return -1

        return {'coin':coins, 'price': price, 'out':bank_out}

    # TODO add fiat
    def getP2PPriceBuy(self, fiat, payType, asset, trade_type, transAmount):
        #return self.binance_controller.getPricePtP(fiat, payType, asset, trade_type, transAmount)
        price = self.binance_controller.getPricePtP(fiat, payType, asset, trade_type, transAmount)
        if price == -1:
            return -1
        #out = 0
        #if trade_type == "SELL":
        #out = transAmount * price
        #else:
        out = transAmount / price
        return {'coin': asset, 'price':price, 'out': out}

    def getP2PPriceSell(self, fiat, payType, asset, trade_type, transAmount):
        #return self.binance_controller.getPricePtP(fiat, payType, asset, trade_type, transAmount)
        price = self.binance_controller.getPricePtP(fiat, payType, asset, trade_type, transAmount)
        if price == -1:
            return -1
        #out = 0
        #if trade_type == "BUY":
        #    out = transAmount / price
        #else:
        out = transAmount * price
        return {'coin': asset, 'price':price, 'out': out}

    def getBestPricesBestChangeForBuy(self, fiat:str, coin:str, transAmount:str, bank:str, id_connection: int):
        #return self.best_change_controller.getBestPriceExch(fiat, coin, transAmount, bank, True)
        prices = self.best_change_controller.getBestPriceExch(fiat, coin, transAmount, bank, True, id_connection)

        if prices == -1:
            return -1

        mas = []
        for pr in range(len(prices)):
            data = {}
            price = float(prices[pr][0])
            bank_out = transAmount / price
            if price == 1:
                price = prices[pr][3]
                bank_out = transAmount*price

            data["exch"] = prices[pr][2]
            data["price"] = price
            data["out"] = bank_out
            mas.append(data)
        return mas
    
    def getBestPricesBestChangeForSell(self, fiat:str, coin:str, transAmount:str, bank:str, id_connection: int):
        #return self.best_change_controller.getBestPriceExch(fiat, coin, transAmount, bank, False)
        prices = self.best_change_controller.getBestPriceExch(fiat, coin, transAmount, bank, False, id_connection)
        
        if prices == -1:
            return -1
        mas = []
        for pr in range(len(prices)):
            data = {}
            price = prices[pr][0]
            bank_out = transAmount*float(price)
            if price == 1:
                price = prices[pr][3]
                bank_out = transAmount/float(price)
            
                    #print(f"            Exch: {prices3[pr][2]}; Price: {price3}; Out: {bank_out3}")
            data["exch"] =  prices[pr][2]
            data["price"] = price
            data["out"] = bank_out
            mas.append(data)

        return mas