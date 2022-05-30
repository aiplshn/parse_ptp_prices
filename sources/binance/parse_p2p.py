from sre_constants import MIN_UNTIL
import gspread
import httplib2
from googleapiclient import discovery
from gspread_dataframe import get_as_dataframe
from oauth2client.service_account import ServiceAccountCredentials
import sys
sys.path.append('../sources')
import toList as toList
import datetime
import math


class GoogleSheetsParse:
    def __init__(self) -> None:
        self.scope = ['https://www.googleapis.com/auth/drive',
                      'https://www.googleapis.com/auth/spreadsheets']
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name(
                            'sources/google_key/creg.json',
                            self.scope)
        self.google_spreadsheet_connection = gspread.authorize(self.credentials)
        self.wks = self.google_spreadsheet_connection.open("binance test")
        self.worksheet = self.wks.get_worksheet(0)
        self.df = get_as_dataframe(self.worksheet, evaluate_formulas=True, index='false')

        # I added below script.
        self.service = discovery.build(
                        'sheets', 'v4', http=self.credentials.authorize(httplib2.Http()))

        self.spreadsheet_id = '1QMxvbXklco9pNASv2KMW2crpyXp5FJzif01HLcXgKrI'  # Please set the Spreadsheet ID here.
        self.ranges = ['Лист2!A11:V20']  # For example, when you want to retrieve the note from the cells "A2:B" of "Sheet1", please use this.

        self.fields = 'sheets(data(rowData(values(note,userEnteredValue))))'
        self.request = self.service.spreadsheets().get(
                        spreadsheetId=self.spreadsheet_id, ranges=self.ranges, fields=self.fields)
        self.update()

    def update(self):
        self.response = self.request.execute()

    def getData(self):
        return self.response
    

class P2PParse:
    def __init__(self) -> None:
        self.google_sheets_parse = GoogleSheetsParse()
        self.parseData()
    
    def getAllData(self):
        return self.data_list

    def getTimeLastUpdate(self):
        return datetime.timedelta(hours=self.hour, minutes=self.minute, seconds=self.second)

    #TODO add fiat
    def getPrice(self, payType, asset, trade_type, transAmount):
        if transAmount == 1000:
            return self.data_list[payType][asset][trade_type]["few"]
        else:
            return self.data_list[payType][asset][trade_type]["lot"]

    def update(self) -> bool:
        now = datetime.datetime.now().time()
        now_time = datetime.timedelta(hours=now.hour, minutes=now.minute, seconds=now.second)
        update_time = datetime.timedelta(hours=self.hour, minutes=self.minute, seconds=self.second)
        delta = now_time - update_time
        if delta.seconds / 60 > 10:
            self.parseData()
            return True
        else:
            return False

    def parseData(self):
        self.data = self.google_sheets_parse.getData()
        self.data_list = toList.toList(self.data)
        self.num_date = self.data['sheets'][0]['data'][0]["rowData"][0]['values'][1]['userEnteredValue']['numberValue']
        hours = self.num_date * 24
        minutes = hours % 1 * 60
        seconds = minutes % 1 * 60
        self.hour = math.floor(hours)
        self.minute = math.floor(minutes)
        self.second = math.floor(seconds)


if __name__ == "__main__":
    pp = P2PParse()
    pp.update()
    data = pp.getAllData()
    print (data)