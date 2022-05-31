from download_best_change import DownloadBestChange
from bc_to_sqlite import BestChangeToSqlite
from exchenges_bc import BestChangeDB
from db import DataBase

# Класс контролер best_change
class BCController():
    def __init__(self) -> None:
        self.dbc = DownloadBestChange()
        self.db = DataBase()
        self.bcts = BestChangeToSqlite(self.db.getCur())
        self.bcdb = BestChangeDB(self.db.getCur())
        self.update()

    def update(self):
        if self.dbc.update():
            self.bcts.update()
        
    def getBestPriceExch(self, fiat:str, coin:str, transAmount:str, bank:str):
        return self.bcdb.getPrice(fiat, coin, transAmount, bank)


if __name__ == "__main__":
    bcc = BCController()
    print(bcc.getBestPriceExch("RUB", "USDT", "10000", "Тинькофф"))