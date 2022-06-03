import sqlite3
import csv
import bc_to_sqlite


#Класс работы с бд
class BestChangeDB:
    def __init__(self, cur) -> None:
        self.cur = cur
    
    def getPrice(self, fiat:str, coin:str, transAmount:str, bank:str, buy:bool):
        # 1. Получить id fiat
        # 2. Получить id coin (несколько)
        # 3. Найти наилучший курс и выдать обменник (Учесть резерв и сумму)
            
        query_buy = f"""
            select MIN(r.price_given) as min_price, c.coin_name, e.name_exch, r.price_assept
            from rates as r
            left join currency as c on r.id_assept_cur = c.id
            left join exchanges as e on  r.id_exch = e.id
            where r.id_given_cur in
            (select id from currency where coin like "{fiat}%{bank}%")
            and r.id_assept_cur in
            (select id from currency where coin like "{coin}%")
            and r.min_sum <= {transAmount} and r.id_town = 0 GROUP BY r.id_assept_cur"""

        query_sell = f"""
            select MAX(r.price_assept) as min_price, c.coin_name, e.name_exch, r.price_given
            from rates as r
            left join currency as c on r.id_given_cur = c.id
            left join exchanges as e on  r.id_exch = e.id
            where r.id_assept_cur in
            (select id from currency where coin like "{fiat}%{bank}%")
            and r.id_given_cur in
            (select id from currency where coin like "{coin}%")
            and r.min_sum <= {transAmount} and r.id_town = 0 GROUP BY r.id_given_cur
        """
        if buy:
            self.cur.execute(query_buy)
        else:
            self.cur.execute(query_sell)
        data = self.cur.fetchall()
        if len(data) != 0:
            return data
        else:
            return -1

if __name__ == "__main__":
    bc = BestChangeDB()
    prices = bc.getPrice("RUB", "USDT", 10000, "Тинькофф")
    print(prices)