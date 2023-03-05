import requests

class Exchange:

    def __init__(self, symbol):
        self._baseURI = "https://api.bithumb.com/public/"
        self.headers = {"accept": "application/json"}
        self.symbol = symbol

    def getCandle(self):
        base = self._baseURI + "candlestick/%s_KRW/5m" %self.symbol
        return requests.get(base, headers=self.headers).json()["data"]
    
