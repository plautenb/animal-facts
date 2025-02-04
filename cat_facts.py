from typing import TYPE_CHECKING, Union, List

import requests
from urllib.parse import urlencode
from config import BASE_URL
from requests_operations import DataOperations

if TYPE_CHECKING:
    from my_dataclasses import CatFact


class CatFacts:
    def __init__(self,
                 animal_type: str,
                 amount: int,
                 random: bool = True):
        self.animal_type = animal_type
        self.amount = amount
        self.random = random

    @staticmethod
    def get_url(animal_type: str, amount:int, random):
        base_url = f"{BASE_URL}/facts"
        params = {"animal_type": animal_type, "amount": str(amount)}
        if random:
            base_url = base_url + "/random?"
        return base_url + urlencode(params)

    def get_cats_facts(self)-> Union['CatFact', List['CatFact']]:
        url = self.get_url(self.animal_type, self.amount, self.random)
        response = requests.get(url)
        data = response.json()
        return DataOperations.from_data(data)

