import os
import requests
import datetime


class FlightSearch:

    def __init__(self):
        self.endpoint = "https://tequila-api.kiwi.com"
        self.token = os.environ['KIWI_KEY']
        self.header = {"apikey": self.token}

    def get_iata(self, city_name):
        iata_url = f"{self.endpoint}/locations/query"
        parameters = {"term": city_name, "location_types": "city"}
        response = requests.get(url=iata_url, params=parameters, headers=self.header)
        return response.json()['locations'][0]['code']

    def get_price(self, origin, destination):
        price_url = f"{self.endpoint}/v2/search"
        parameters = {
            "fly_from": origin,
            "fly_to": destination,
            "date_from": datetime.datetime.now().strftime("%d/%m/%Y"),
            "date_to": (datetime.datetime.now()+datetime.timedelta(weeks=26)).strftime("%d/%m/%Y"),
            "vehicle_type": "aircraft",
            "sort": "price"
        }
        response = requests.get(url=price_url, params=parameters, headers=self.header)
        return response.json()['data'][0]
