import sqlite3
import csv

#Класс записи в БД информации обменников
class BestChangeToSqlite:
    def __init__(self) -> None:
        self.con = sqlite3.connect('data/data.db')
        self.cur = self.con.cursor()
        self.update()
        
    def update(self):
        self.parseCurrency()
        self.parseExch()
        self.parseRates()

    def __del__(self):
        self.con.commit()
        self.con.close()

    def parseCurrency(self):
        file = open('data/bm_cy.dat')
        rows = csv.reader(file, delimiter=';')
        self.cur.execute('DELETE FROM currency')
        self.cur.executemany('INSERT INTO currency VALUES (?,?,?,?,?,?,?)', rows)
        self.cur.fetchall()

    def parseRates(self):
        file = open('data/bm_rates.dat')
        rows = csv.reader(file, delimiter=';')
        self.cur.execute('DELETE FROM rates')
        self.cur.executemany('INSERT INTO rates VALUES (?,?,?,?,?,?,?,?,?,?,?)', rows)
        self.cur.fetchall()

    def parseExch(self):
        file = open('data/bm_exch.dat')
        rows = csv.reader(file, delimiter=';')
        self.cur.execute('DELETE FROM exchanges')
        self.cur.executemany('INSERT INTO exchanges VALUES (?,?,?,?,?)', rows)
        self.cur.fetchall()


if __name__ == "__main__":
    bc = BestChangeToSqlite()