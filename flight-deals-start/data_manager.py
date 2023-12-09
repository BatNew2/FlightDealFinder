import requests
class DataManager:
    def __init__(self):
        self.response = requests.get("https://api.sheety.co/b3d5e792cbcb8a687f1186193cb7e04c/flightDeals/prices")
        self.response.raise_for_status()
        self.data = self.response.json()
        self.data = [[city["from"], city["iataCode"], city["lowestPrice"], city['city']] for city in self.data["prices"]]
