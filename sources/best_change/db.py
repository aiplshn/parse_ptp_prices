import sqlite3

class DataBase:
    def __init__(self) -> None:
        self.con = sqlite3.connect('data/data.db')
        self.cur = self.con.cursor()
    
    def getCur(self):
        return self.cur

    def __del__(self):
        self.con.commit()
        self.con.close()