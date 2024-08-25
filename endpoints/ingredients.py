from urls import *
import requests
import allure


class Ingredients:

    def __init__(self):
        self.json = requests.get(ingredients_url).json()

    @allure.step('Получаем ингредиенты')
    def get_ingredients(self):
        return self.json

    @allure.step('Получаем список хешей ингредиентов')
    def get_ingredients_id_list(self):
        ids = []
        for i in self.json['data']:
            ids.append(i['_id'])
        return ids
