import sqlite3

class DataBase:
    def __init__(self) -> None:
        self.path = 'parse_best_change/data/data.db'
    
    def getCur(self):
        return self.cur

    def closeConnection(self):
        self.con.close()

    def openConnection(self):
        self.con = sqlite3.connect(self.path)
        self.cur = self.con.cursor()

    def commitChanges(self):
        self.con.commit()