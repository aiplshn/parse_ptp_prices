import sys
sys.path.append('sources')
sys.path.append('sources/best_change')
sys.path.append('sources/binance')
from parse_best_change.sources.controller_prices import ControllerPrices
from parse_best_change.sources.coins import coins
from parse_best_change.sources import banks

# Класс поиска связок
def Spreed(bank_before, bank_after):
    return (bank_after/bank_before-1)*100

class Bundles:

    def __init__(self, id_connection) -> None:
        self.id_connection = id_connection

    def Bundle1(self, cp:ControllerPrices, bank:float, fiat:str, bank_name: str, buy: str, spd:float):
        #Банк-P2P-Спот-Обменник2-Банк
        outs = {}
        for coin1 in coins:
            priceP2P = cp.getP2PPriceBuy(fiat, bank_name, coin1, buy, bank) #{}
            if priceP2P == -1:
                continue
            
            for coin2 in coins:
                # priceSpot = {}
                if coin1 == 'RUB' and coin2 == 'SHIB':
                    continue
                priceSpot = cp.getSpotPrice(coin1, coin2, priceP2P['out']) #{}
                if priceSpot == -1:
                    continue
                priceExch = cp.getBestPricesBestChangeForSell(fiat, coin2, priceSpot['out'], banks.get_banks_bc_from_binance(bank_name), self.id_connection) #[]
                if priceExch == -1:
                    continue
                priceSpot['exchs'] = priceExch
                priceP2P[coin2] = priceSpot
            outs[coin1] = priceP2P

        mas = []
        for key1 in outs:
            for key2 in outs[key1]:
                for coin in coins:
                    if coin == key2:
                        for exch in outs[key1][key2]['exchs']:
                            if exch['out'] > bank:
                                spreed = (exch['out']/bank-1)*100
                                if spreed < spd:
                                    continue
                                mes = f"""Покупка на P2P {key1} по курсу {outs[key1]['price']} -> {outs[key1]['out']}
    Обмен на споте на {key2} по курсу {outs[key1][key2]['price']} -> {outs[key1][key2]['out']}
    Продажа на BestChange: обменник {exch['exch']} по курсу {exch['price']}
    Получаем {exch['out']}
    Спред: {spreed}"""
                                mas.append(mes)
        return mas

    def Bundle2(self, cp:ControllerPrices, bank:float, fiat:str, bank_name: str, spd:float):
        #Банк-Обменник-P2P-Банк
        outs = {}
        for coin1 in coins:
            if coin1 == 'SHIB':
                continue
            priceExch = cp.getBestPricesBestChangeForBuy(fiat, coin1, bank, banks.get_banks_bc_from_binance(bank_name), self.id_connection) #[]
            if priceExch == -1:
                continue
            for i in priceExch:
                priceP2P = cp.getP2PPriceSell(fiat, bank_name, coin1, "BUY", i['out']) #{}
                if priceP2P == -1:
                    continue
                i['p2p'] = priceP2P
            outs[coin1] = priceExch

        # print(outs)
        mas = []
        for key1 in outs.keys():
            for exch in outs[key1]:
                if exch['p2p']['out'] > bank:
                    spreed = Spreed(bank, exch['p2p']['out'])
                    if spreed < spd:
                        continue
                    mes = f"""Покупаем {key1} на BestChange: обменник {exch['exch']} по курсу {exch['price']} -> {exch['out']}
    Продаем {key1} на P2P по курсу {exch['p2p']['price']}
    Получаем {exch['p2p']['out']}
    Спред {spreed}"""
                    mas.append(mes)
        return mas

    def Bundle3(self, cp:ControllerPrices, bank:float, fiat:str, bank_name: str, spd:float):
        #Банк-Обменник-Спот-Обменник2-Банк
        outs = {}
        for coin1 in coins:
            priceExch1 = cp.getBestPricesBestChangeForBuy(fiat, coin1, bank, banks.get_banks_bc_from_binance(bank_name), self.id_connection) #[]
            if priceExch1 == -1:
                continue
            if coin1 == fiat:
                continue
            for exch1 in priceExch1:
                priceSpot = {}
                for coin2 in coins:
                    if coin1 == 'RUB' and coin2 == 'SHIB':
                        continue
                    priceSpot = cp.getSpotPrice(coin1, coin2, exch1['out']) #{}
                    if priceSpot == -1:
                        continue
                    priceExch2 = cp.getBestPricesBestChangeForSell(fiat, coin2, priceSpot['out'], banks.get_banks_bc_from_binance(bank_name), self.id_connection) #[]
                    if priceExch2 == -1:
                        continue
                    priceSpot['exchs'] = priceExch2
                    exch1[coin2] = priceSpot
            outs[coin1] = priceExch1
        # print(outs)
        mas = []
        for key1 in outs.keys():
            for exch1 in outs[key1]:
                for coin1 in coins:
                    if coin1 in exch1.keys():
                        for exch2 in exch1[coin1]['exchs']:
                            if exch2['out'] > bank:
                                spreed = Spreed(bank, exch2['out'])
                                if spreed < spd:
                                    continue
                                mes = f"""Покупаем {key1} на BestChange: обменник {exch1['exch']} по курсу {exch1['price']} -> {exch1['out']}
    Обмен на споте на {coin1} по курсу {exch1[coin1]['price']} -> {exch1[coin1]['out']}
    Продаем на BestChange: обменник {exch2['exch']} по курсу {exch2['price']}
    Получаем {exch2['out']}
    Спред {spreed}"""
                                mas.append(mes)
        return mas

    def Bundle4(self, cp:ControllerPrices, bank:float, fiat:str, bank_name: str, spd:float):
        #Банк-Обменник-Спот-P2P-Банк
        outs = {}
        for coin1 in coins:
            priceExch = cp.getBestPricesBestChangeForBuy(fiat, coin1, bank, banks.get_banks_bc_from_binance(bank_name), self.id_connection) #[]
            if priceExch == -1:
                continue
            if fiat == coin1:
                continue
            for exch in priceExch:
                priceSpot = {}
                for coin2 in coins:
                    if coin1 == 'RUB' and coin2 == 'SHIB':
                        continue
                    priceSpot = cp.getSpotPrice(coin1, coin2, exch['out']) #{}
                    if priceSpot == -1:
                        continue
                    priceP2P = cp.getP2PPriceSell(fiat, bank_name, coin2, "BUY", priceSpot['out']) #{}
                    if priceP2P == -1:
                        continue
                    priceSpot['p2p'] = priceP2P
                    exch[coin2] = priceSpot
            outs[coin1] = priceExch

        # print(outs)
        mas = []
        for key1 in outs.keys():
            for exch1 in outs[key1]:
                for coin1 in coins:
                    if coin1 in exch1.keys():
                        if exch1[coin1]['p2p']['out'] > bank:
                            spreed = Spreed(bank, exch1[coin1]['p2p']['out'])
                            if spreed < spd:
                                continue
                            mes = f"""Покупаем {key1} на BestChange: обменник {exch1['exch']} по курсу {exch1['price']} -> {exch1['out']}
    Обмен на споте на {coin1} по курсу {exch1[coin1]['price']} -> {exch1[coin1]['out']}
    Продаем на P2P по курсу {exch1[coin1]['p2p']['price']} 
    Получаем {exch1[coin1]['p2p']['out']}
    Спред {spreed}"""
                            mas.append(mes)
        return mas

    def Bundle5(self, cp:ControllerPrices, bank:float, fiat:str, bank_name: str, buy: str, spd:float):
        #Банк-P2P-Спот-P2P-Банк
        outs = {}
        for coin1 in coins:
            priceP2P = cp.getP2PPriceBuy(fiat, bank_name, coin1, buy, bank) #{}
            if priceP2P == -1:
                continue
            
            for coin2 in coins:
                # priceSpot = {}
                if coin1 == 'RUB' and coin2 == 'SHIB':
                    continue
                priceSpot = cp.getSpotPrice(coin1, coin2, priceP2P['out']) #{}
                if priceSpot == -1:
                    continue
                priceP2P2 = cp.getP2PPriceSell(fiat, bank_name, coin2, "BUY", priceSpot['out']) #{}
                if priceP2P2 == -1:
                    continue
                priceSpot['p2p'] = priceP2P2
                priceP2P[coin2] = priceSpot
            outs[coin1] = priceP2P

        # print(outs)

        mas = []
        for key1 in outs:
            for coin in coins:
                if coin in outs[key1]:
                    if outs[key1][coin]['p2p']['out'] > bank:
                        spreed = Spreed(bank, outs[key1][coin]['p2p']['out'])
                        if spreed < spd:
                            continue
                        mes = f"""Покупка на P2P {key1} по курсу {outs[key1]['price']} -> {outs[key1]['out']}
    Обмен на споте на {coin} по курсу {outs[key1][coin]['price']} -> {outs[key1][coin]['out']}
    Продажа {outs[key1][coin]['p2p']['coin']} на P2P по курсу {outs[key1][coin]['p2p']['price']}
    Получаем {outs[key1][coin]['p2p']['out']}
    Спред: {spreed}"""
                        mas.append(mes)
        return mas

    def Bundle6(self, cp:ControllerPrices, bank:float, fiat:str, bank_name: str, buy: str, spd:float):
        #Банк-P2P-Обменник-Банк
        outs = {}
        for coin1 in coins:
            priceP2P = cp.getP2PPriceBuy(fiat, bank_name, coin1, buy, bank) #{}
            if priceP2P == -1:
                continue
            priceExch = cp.getBestPricesBestChangeForSell(fiat, coin1, priceP2P['out'], banks.get_banks_bc_from_binance(bank_name), self.id_connection)
            if priceExch == -1:
                continue
            priceP2P['exchs'] = priceExch
            outs[coin1] = priceP2P

        # print(outs)

        mas = []
        for key1 in outs:
            for exch in outs[key1]['exchs']:
                if exch['out'] > bank:
                    spreed = Spreed(bank, exch['out'])
                    if spreed < spd:
                        continue
                    mes = f"""Покупка на P2P {key1} по курсу {outs[key1]['price']} -> {outs[key1]['out']}
    Продаем на BestChange: обменник {exch['exch']} по курсу {exch['price']}
    Получаем {exch['out']}
    Спред: {spreed}"""
                    mas.append(mes)
        return mas

    def Bundle7(self, cp:ControllerPrices, bank:float, fiat:str, bank_name: str, buy: str, spd:float):
        #Банк-P2P-P2P-Банк
        outs = {}
        for coin1 in coins:
            priceP2P1 = cp.getP2PPriceBuy(fiat, bank_name, coin1, buy, bank) #{}
            if priceP2P1 == -1:
                continue
            priceP2P2 = cp.getP2PPriceSell(fiat, bank_name, coin1, "BUY", priceP2P1['out'])
            if priceP2P2 == -1:
                continue
            priceP2P1['p2p2'] = priceP2P2
            outs[coin1] = priceP2P1

        mas = []
        for key1 in outs:
            if outs[key1]['p2p2']['out'] > bank:
                spreed = Spreed(bank, outs[key1]['p2p2']['out'])
                if spreed < spd:
                    continue
                mes = f"""Покупка на P2P {key1} по курсу {outs[key1]['price']} -> {outs[key1]['out']}
    Продаем на P2P {key1} по курсу {outs[key1]['p2p2']['price']}
    Получаем {outs[key1]['p2p2']['out']}
    Спред: {spreed}"""
                mas.append(mes)
        return mas

def FindAllBundles(cp:ControllerPrices, bank:float, fiat:str, bank_name: str, tp1: bool, spreed: float, id_connection: int):
    # id_con = cp.newConnection()
    buy = ''
    if tp1:
        buy = 'BUY'# Купить
    else:
        buy = 'SELL'

    mas = []
    bundles = Bundles(id_connection)
    mas.append(bundles.Bundle1(cp, bank, fiat, bank_name, buy, spreed))
    mas.append(bundles.Bundle2(cp, bank, fiat, bank_name, spreed)) #нет P2P, поэтому не передаём buy
    mas.append(bundles.Bundle3(cp, bank, fiat, bank_name, spreed))
    mas.append(bundles.Bundle4(cp, bank, fiat, bank_name, spreed))
    mas.append(bundles.Bundle5(cp, bank, fiat, bank_name, buy, spreed))
    mas.append(bundles.Bundle6(cp, bank, fiat, bank_name, buy, spreed))
    mas.append(bundles.Bundle7(cp, bank, fiat, bank_name, buy, spreed))
    # cp.closeConnection(id_con)
    return mas