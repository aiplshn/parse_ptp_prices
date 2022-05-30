from operator import ge
from best_change import parse_bestchange
import coins
from binance import parse_binance

def findWallet(wallets, wallet):
    for i in wallets:
        if wallets[i][2].find(wallet) != -1:
            yield i, wallets[i][2]

def parseCur(all_name_cur:str):
    for i in coins.coins:
        if all_name_cur.find(i) != -1:
            return i
    

if __name__ == "__main__":
    fiat = input("Введите валюту: ")
    bc = parse_bestchange.BestChange()
    #bc.update()
    bc.parse()
    wallets = bc.getAllWallet()
    for i in wallets:
        print(wallets[i][2])
    
    find_flag = False
    while not find_flag:
        wallet = input("Выберите ваш кошелек/банк\n")
        gen = findWallet(wallets, wallet)
        id_wallet = -1
        
        while True:
            try:
                idx, findwallet = next(gen)
                if input("Это ваш кошелек/банк: "+ findwallet + "\nY/N: ").upper() == "y".upper():
                    id_wallet = idx
                    find_flag = True
                    break
            except StopIteration:
                print("НЕ НАЙДЕНО")
                break


    bank = int(input("Введите сумму:\n"))
    # Перебор всех валют
    print("ID: "+ str(wallets[idx][0]))
    res = {}
    res['value'] = 0
    res['out'] = 0
    count_crypt = 1
    for i in coins.coins:
        #print(str(count_crypt) + "/" + str(len(coins.coins)))
        count_crypt += 1
        gen = bc.getIdWallet(fiat=i) # ID валюты
        while True:
            try:
                cur = next(gen) 
                id_rate, exch = bc.findBestExch(wallets[idx][0], cur)
                if exch == "Quickex":
                    continue
                if id_rate == "-1":
                    continue
                res['value'] = bank/float(bc.getRate(id_rate)[3])
                # Купили другую валюту 
                # TODO: Парсить курс бинанса с валютами fiat и name_cur!!!
                name_cur = bc.getNameCur(cur)
                if name_cur not in coins.coins:
                    continue

                cource = parse_binance.getPrice(fiat, name_cur)
                if cource != -1:
                    print("Обменник:" + exch + " Валюта: " + name_cur + " Курс: " + str(bc.getRate(id_rate)[3]) + " Получаем: " + str(res['value']) + " Продаём: " + cource['symbol'] + " По курсу: " + cource['price'])
                    # + "("+ cource['symbol'] +")" + ": " + str(cource['price']))
                    idx_str = cource['symbol'].find(fiat)
                    value_tmp = 0
                    if idx_str != 0:
                        value_tmp = float(cource['price'])*res['value']
                    else:
                        value_tmp = res['value']/float(cource['price'])
                    print("Выход: " + str(value_tmp))
                    if float(res['out']) < value_tmp:
                        res['exch'] = exch
                        res['cur'] = name_cur
                        res['id_rate'] = id_rate
                        res['symbol'] = cource['symbol']
                        res['price'] = str(cource['price'])
                        res['out'] = str(value_tmp)
                        res['spred'] = str((value_tmp/bank-1)*100)
                    # symbol
            except StopIteration:
               break
    print("--------------------------------------------")
    print("RESULT (связка кошелек - обменник - бинанс):")
    print("Обменник: " + res['exch'])
    print("Валюта: " + res['cur'])
    print("Курс: " + str(bc.getRate(res['id_rate'])[3]))
    print("Получили на бинанс: " + str(res['value']))
    print("Меняем: " + str(res['symbol']))
    print("По курсу: " + str(res['price']))
    print("Выход: " + str(res['out']))
    print("СПРЕД: " + str(res['spred']))
        
    # RUB / ETH, RUB / BTC ...

# Банк - Обменник - БинансP2P - Банк
# Банк - БинансP2P - Обменник - Банк
# Банк - БинансP2P - БинансP2P- Банк

# Банк - Обменник - БинансSpot - БинансP2P - Банк
# Банк - БинансP2P - БинансSpot - Обменник - Банк
# Банк - БинансP2P - БинансSpot - БинансP2P- Банк

