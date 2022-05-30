import requests, zipfile
from io import BytesIO as si
import csv
import datetime

#Класс скачивания архива и чтения обменников
class DownloadBestChange:
    def __init__(self) -> None:
        self.timeout = 60
        self.zip_file_url = "http://api.bestchange.ru/info.zip"
        self.first_update = True


    def update(self) -> bool:
        time_delta = 0
        if self.first_update:
            self.first_update = False
        else:
            self.time_now = datetime.datetime.now()
            time_delta = self.time_now - self.time_update
            if time_delta.seconds < self.timeout:
                return False

        r = requests.get(self.zip_file_url, stream=True)
        z = zipfile.ZipFile(si(r.content))
        z.extractall("../data")
        self.time_update = datetime.datetime.now()
        return True


#TODO: delete this
#Заменил на БД
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

        self.exch = {} # Обменники
        with open("./data/bm_exch.dat", encoding="cp1251") as file:
            file_reader = csv.reader(file, delimiter = ";")
            for row in file_reader:
                self.exch[int(row[0])] = row[1]

        self.rates = {} # Курсы
        with open("./data/bm_rates.dat", encoding="cp1251") as file:
            file_reader = csv.reader(file, delimiter = ";")
            count = 0
            for row in file_reader:
                self.rates[count] = row
                count += 1


if __name__ == '__main__':
    time_update = datetime.datetime(year=2022, month=5, day=28,hour=17,minute=0)
    time_now = datetime.datetime.now()

    time_delta = time_now - time_update
    print (time_delta.seconds)
        