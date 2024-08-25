from urls import *
import requests
import allure
import json


class Orders:

    def __init__(self):
        self.accessToken = None

    @allure.step('Создаем заказ')
    def create_order(self, ingredients):
        headers = {
            'Content-Type': 'application/json'
        }
        if self.accessToken:
            headers['authorization'] = self.accessToken

        payload = {}
        if ingredients:
            payload['ingredients'] = ingredients

        response = requests.post(orders_url, data=json.dumps(payload), headers=headers)
        return response

    @allure.step('Получаем список заказов')
    def get_orders(self):
        headers = {
            'Content-Type': 'application/json'
        }
        if self.accessToken:
            headers['authorization'] = self.accessToken

        response = requests.get(orders_url, headers=headers)
        return response
