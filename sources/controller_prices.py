from best_change.controller_bc import BCController
from binance.binanceController import ControllerBinance

# Класс контролер курсов
class ControllerPrices:
    def __init__(self):
        self.best_change_controller = BCController()
        self.binance_controller = ControllerBinance()
        self.update()

    def update(self):
        self.best_change_controller.update()
        self.binance_controller.update()

    def getSpotPrice(self, fiat:str, coin:str):
        return self.binance_controller.getPriceSpot(fiat, coin)

    # TODO add fiat
    def getP2PPrice(self, fiat, payType, asset, trade_type, transAmount):
        return self.binance_controller.getPricePtP(fiat, payType, asset, trade_type, transAmount)
    
    def getBestPricesBestChange(self, fiat:str, coin:str, transAmount:str, bank:str):
        return self.best_change_controller.getBestPriceExch(fiat, coin, transAmount, bank)