import requests
import os


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheet_token = os.environ['SHEET_TOKEN']
        self.sheet_url = f"https://api.sheety.co/{os.environ['SHEET_USERNAME']}/flightDeals/prices"
        self.header = {"Authorization": f"Bearer {self.sheet_token}"}

    def get_data(self):
        data = requests.get(url=self.sheet_url, headers=self.header)
        return data.json()

    def update_row(self, row_id, data):

        update = requests.put(url=f"{self.sheet_url}/{row_id}", json=data, headers=self.header)
        print(update.text)
