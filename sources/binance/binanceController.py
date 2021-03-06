from parse_best_change.sources.binance.parse_binance import ParseBinanceSpot
from parse_best_change.sources.binance.parse_p2p import P2PParse

# Класс контролер Binance
class ControllerBinance:
    def __init__(self) -> None:
        self.pbs = ParseBinanceSpot()
        self.ptp = P2PParse()
        self.update()

    def update(self):
        self.pbs.update()
        self.ptp.update()

    def getPriceSpot(self, fiat:str, coin:str):
        return self.pbs.getPrice(fiat, coin)

    def getAllSpotPrice(self):
        return self.pbs.getAllPrice()

    # TODO add fiat
    # Логика оптово-розничной продажи
    def getPricePtP(self, fiat, payType, asset, trade_type, transAmount):
        return self.ptp.getPrice(payType, asset, trade_type, transAmount)
        if trade_type == "SELL":
            pass
        # если продать
        # получить наибольшую цену из [few] и [lot]
        # 

    def getAllPtPPrice(self):
        return self.ptp.getAllData()

if __name__ == "__main__":
    cb = ControllerBinance()
    print(cb.getPricePtP("RUB", "RosBank", "BTC1","SELL", 10000))
    print(cb.getPriceSpot("RUB", "BTC"))