import json
import os
import requests


class MarketApi:

    def __init__(self):
        self.api_url = os.getenv("CSGO_MARKET_API_URL")
        self.api_token = os.getenv("CSGO_MARKET_API_TOKEN")

    def get_item(self, item_id):
        response = requests.get("{api_url}/item/{item_id}".format(api_url=self.api_url, item_id=item_id),
                                headers={"x-token": self.api_token})
        return response.json()
