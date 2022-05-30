import sqlite3
import csv
import bc_to_sqlite


#Класс работы с бд
class BestChangeDB:
    def __init__(self) -> None:
        self.con = sqlite3.connect('data/data.db')
        self.cur = self.con.cursor()
    
    def getPrice(self, fiat, coin, transAmount, bank):
        fiat = str(fiat)
        coin = str(coin)
        transAmount = str(transAmount)
        self.cur.execute(f"SELECT ")
        pass