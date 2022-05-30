import enum

class columnsCurrency(enum.Enum):
    ID = 0
    ID_BEST_CHANGE = 1
    COIN_NAME = 2
    COIN = 3
    TMP1 = 4
    TMP2 = 5
    TMP3 = 6

class columnsRates(enum.Enum):
    ID_GIVEN_CUR = 0
    ID_ASSEPT_CUR = 1
    ID_EXCHENGES = 2
    PRICE_GIVEN = 3
    PRICE_ASSEPT = 4
    RESERVE_CUR = 5
    REVIEW = 6
    MIN_SUM = 8
    MAX_SUM = 9
    ID_TOWN = 10

class columnsExchenges(enum.Enum):
    ID = 0
    NAME_EXCH = 1