import requests
from datetime import datetime


class FlightSearch:
    def __init__(self, data):
        self.prices = []
        self.HEADER = {
            "apikey": "RtZv8SYl0Xezf2egd8gYBkgwT7o6tSg_"
        }
        self.now = datetime.now()
        self.future = str(self.now).split(" ")
        self.future = str(self.future[0]).split("-")
        self.future[1] = int(self.future[1])
        self.future[1] += 6
        if self.future[1] > 12:
            self.future[1] -= 12
            self.future[0] = int(self.future[0]) + 1
        self.future[1] = str(self.future[1])
        if len(self.future[1]) == 1:
            self.future[1] = f"0{self.future[1]}"
        self.future = f"{self.future[2]}/{self.future[1]}/{self.future[0]}"

        for dt in data:
            self.query = {
                "fly_from": dt[0],
                "fly_to": dt[1],
                "date_from": f"{self.now.strftime('%d')}/{self.now.strftime('%m')}/{self.now.strftime('%Y')}",
                "date_to": self.future,
                "limit": 1
            }
            self.response = requests.get("https://api.tequila.kiwi.com/v2/search/", headers=self.HEADER, params=self.query)
            self.response.raise_for_status()
            self.data = self.response.json()
            print(self.response.json())
            self.prices.append([dt[1], self.data["data"][0]["price"], self.data["data"][0]["deep_link"], self.data["data"][0]["local_departure"]])
