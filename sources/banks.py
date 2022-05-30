# Названия банков в бинансе и bestChange
# И перевод 

banks_binance = ["Tinkoff",  "QIWI", "YandexMoney", "RosBank",  "RUBfiatbalance"]
banks_bc      = ["Тинькофф", "QIWI", "ЮMoney",      "Сбербанк", "Binance"]


def get_banks_bc_from_binance(bank):
    for i in banks_binance:
        if i == bank:
            idx = banks_binance.index(i)
            return banks_bc[idx]

def get_banks_binance_from_bc(bank):
    for i in banks_bc:
        if i == bank:
            idx = banks_bc.index(i)
            return banks_binance[idx]

if __name__ == "__main__":

    bc = get_banks_bc_from_binance("RosBank")
    print(bc)
    b = get_banks_binance_from_bc("Сбербанк")
    print(b)