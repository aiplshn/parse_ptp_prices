import requests, zipfile
from io import BytesIO as si
import csv

#TODO: завести все данные в БД и работать с ней

class BestChange:
    def __init__(self) -> None:
        self.timeout = 60
        self.zip_file_url = "http://api.bestchange.ru/info.zip"

    def update(self):
        r = requests.get(self.zip_file_url, stream=True)
        z = zipfile.ZipFile(si(r.content))
        z.extractall("../data")
        print("Updating is done")

    def parse(self):
        self.cur = {} # Валюта
        with open("./data/bm_cy.dat", encoding="cp1251") as bm_cy:
            # Создаем объект reader, указываем символ-разделитель ","
            file_reader = csv.reader(bm_cy, delimiter = ";")
            # Считывание данных из CSV файла
            count = 0
            for row in file_reader:
                self.cur[count] = row
                count += 1
        
        print("_______________________Считали валюту_______________________")
        self.exch = {} # Обменники
        with open("./data/bm_exch.dat", encoding="cp1251") as file:
            file_reader = csv.reader(file, delimiter = ";")
            for row in file_reader:
                self.exch[int(row[0])] = row[1]
       
        print("_______________________Считали обменники_______________________")

        self.rates = {} # Курсы
        with open("./data/bm_rates.dat", encoding="cp1251") as file:
            file_reader = csv.reader(file, delimiter = ";")
            count = 0
            for row in file_reader:
                self.rates[count] = row
                count += 1
        print("_______________________Считали курсы_______________________")

    def getExch(self, id):
        return self.exch[id]

    def getNameCur(self, id):
        for i in self.cur.keys():
            if self.cur[i][0] == id:
                return self.cur[i][3]

    def getWallet(self, fiat):
        for i in self.cur:
            dt = self.cur[i]
            if dt[3].find(fiat) != -1:
                yield dt[2]

    def getIdWallet(self, fiat):
        for i in self.cur:
            dt = self.cur[i]
            if dt[3].find(fiat) != -1:
                yield dt[0]

    def getAllWallet(self):
        return self.cur

    def getAllRates(self, id_send, id_recv):

        for k in self.rates.keys():
            if int(self.rates[k][0]) == id_send and int(self.rates[k][1]) == id_recv:
                yield k
        
    def getRate(self, id):
        return self.rates[id]

    def getBestRate(self, id_send, id_recv):
        try:
            all = self.getAllRates(id_send, id_recv)
        except StopIteration:
            return -1
        cource = 9999999999999999#all[0][3]
        idx_best = 0
        for k in all:
            if cource > float(self.rates[k][3]):
                cource = float(self.rates[k][3])
                idx_best = k
        return idx_best

    def getIdExchFromIdRate(self, id_rate):
        return int(self.rates[id_rate][2])

    def findBestExch(self, id_send, id_recv):
        best_rate = self.getBestRate(int(id_send), int(id_recv))
        if best_rate != -1:
            return best_rate, self.getExch(self.getIdExchFromIdRate(best_rate))
        else:
            return "-1", "-1"

if __name__ == "__main__":
    bc = BestChange()
    bc.parse()
    g = bc.getWallet("USDT")
    for res in g:
        print(res)
    print("__________")
    g = bc.getAllRates(170, 36)
    for res in g:
        print(res)
    print("__________")
    print(bc.findBestExch(170, 36))
