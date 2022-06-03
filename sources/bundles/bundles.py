import sys
sys.path.append('sources')
from sources.controller_prices import ControllerPrices
from coins import coins
# Класс поиска связок
class FindBundles:
    def __init__(self) -> None:
        pass

    def getBundle(self):
        pass


if __name__ == "__main__":
    cp = ControllerPrices()
    bank = 10000
    for coin in coins:
        price = cp.getP2PPrice("RUB", "Rosbank", coin, "BUY", bank)
        print(price)
