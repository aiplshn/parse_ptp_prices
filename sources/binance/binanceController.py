from parse_best_change.sources.binance.parse_binance import ParseBinanceSpot
from parse_best_change.sources.binance.parse_p2p import P2PParce

# Класс контролер Binance
class ControllerBinance:

    def getPriceSpot(self, fiat:str, coin:str):
        pbs = ParseBinanceSpot()
        return pbs.getPrice(fiat, coin)

    # Логика оптово-розничной продажи
    def getPricePtP(self, fiat, payType, asset, trade_type, transAmount):
        ptp = P2PParce()
        return ptp.getPrice(fiat, payType, asset, trade_type, transAmount)

if __name__ == "__main__":
    cb = ControllerBinance()
    print(cb.getPricePtP("RUB", "RosBankNew", "BTC","SELL", 10000))
    print(cb.getPriceSpot("RUB", "BTC"))