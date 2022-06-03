import sys
sys.path.append('./')
from parse_best_change.sources.best_change.download_best_change import DownloadBestChange
from parse_best_change.sources.best_change.bc_to_sqlite import BestChangeToSqlite
from parse_best_change.sources.best_change.exchenges_bc import BestChangeDB
from parse_best_change.sources.best_change.db import DataBase

# Класс контролер best_change
class BCController():
    def __init__(self) -> None:
        self.dbc = DownloadBestChange()
        self.bcts = BestChangeToSqlite()
        self.bcdb = BestChangeDB()
        self.pull_db_connection = []
        self.pull_open_db = []
        self.update()
       
    def newConnection(self):
        db = DataBase()
        self.pull_db_connection.append(db)
        db.openConnection()
        self.pull_open_db.append(True)
        return len(self.pull_db_connection) - 1

#TODO когда удаляем индексы меняются
    def closeConnection(self, id: int):
        self.pull_db_connection[id].closeConnection()
        self.pull_open_db[id] = False

    def update(self):
        if self.dbc.update():
            id = self.newConnection()
            self.bcts.update(self.pull_db_connection[id])
            self.pull_db_connection[id].commitChanges()
            self.closeConnection(id)
        
    def getBestPriceExch(self, fiat:str, coin:str, transAmount:str, bank:str, buy:bool, id_connection: int):
        return self.bcdb.getPrice(fiat, coin, transAmount, bank, buy, self.pull_db_connection[id_connection])

    def closeAllConnections(self):
        for i in range(len(self.pull_db_connection)):
            if self.pull_open_db:
                self.pull_db_connection[i].closeConnection()

    # def __del__(self):
    #     for i in self.pull_db_connection:
    #         i.closeConnection()